# Builds the "In-Class Prep Quiz" bank from the lab station photos and swaps
# high-confidence real-model photos into matching existing banks.
import cv2, numpy as np, os, json

ROOT = "C:/Users/produ/muscle-pin-quiz-v2"
SRC  = "C:/Users/produ/Downloads/images"
IMG  = ROOT + "/images"

# EXIF-upright loader
def upright(path):
    from PIL import Image, ImageOps
    im = ImageOps.exif_transpose(Image.open(path))
    return cv2.cvtColor(np.array(im), cv2.COLOR_RGB2BGR)

# per-station: source file, crop box (upright coords), output name
CROP = {
 "s2": ("IMG_5135.jpeg", (840,700,1360,1480)),
 "s3": ("IMG_5134.jpeg", (480,120,1180,1000)),
 "s4": ("IMG_5133.jpeg", (0,700,1200,1090)),
 "s5": ("IMG_5132.jpeg", (520,0,1000,1380)),
 "s6": ("IMG_5131.jpeg", (380,20,1000,1360)),
 "s7": ("IMG_5130.jpeg", (300,40,1400,980)),
}
# pins in UPRIGHT coords, per station, keyed by tag
PINS = {
 "s2": {"Q7":(1050,820), "Q8":(1201,1120)},
 "s3": {"Q9":(941,488),  "Q10":(645,655)},
 "s4": {"Q11":(972,911), "Q12":(300,820), "Q13":(566,790), "Q14":(470,815)},
 "s5": {"Q15":(710,535), "Q16":(650,300), "Q17":(710,535), "Q18":(730,415)},
 "s6": {"Q19":(668,548), "Q20":(796,887)},
 "s7": {"Q21":(560,193), "Q22":(964,260), "NUC":(970,430)},
}

saved = {}   # station -> (filename, w, h)
pinpx = {}    # (station,tag) -> bbox_px

for st,(fn,(x0,y0,x1,y1)) in CROP.items():
    img = upright(os.path.join(SRC, fn))
    crop = img[y0:y1, x0:x1]
    h,w = crop.shape[:2]
    out = f"inclass_{st}.jpg"
    cv2.imwrite(os.path.join(IMG,out), crop, [cv2.IMWRITE_JPEG_QUALITY,88])
    saved[st] = (out,w,h)
    half = max(12, round(0.025*min(w,h)))
    for tag,(px,py) in PINS[st].items():
        cx,cy = px-x0, py-y0
        cx=max(half,min(w-half,cx)); cy=max(half,min(h-half,cy))
        pinpx[(st,tag)] = [cx-half, cy-half, cx+half, cy+half]
    print(st, out, f"{w}x{h}")

def q(st, tag, prompt, answer, pool):
    # `options` = the exact a-e choices printed on the paper card (rendered as-is);
    # `id` = stable key so user-chosen answers/pins survive answer edits.
    fn,w,h = saved[st]
    return {"id":"ic_"+tag.lower(),"image":"images/"+fn,"width_px":w,"height_px":h,
            "bbox_px":pinpx[(st,tag)],"answer":answer,"prompt":prompt,
            "options":pool,"view_label_pool":pool}

WHATM = "What is this muscle?"
WHATM2 = "What muscle is this?"
WHATS = "What is this structure?"
WHATN = "What non-muscular structure is this?"

questions = [
 q("s2","Q7", "Station 2 · "+WHATM, "External intercostal",
   ["Pectoralis major","Pectoralis minor","Innermost intercostal","External intercostal","Internal intercostal"]),
 q("s2","Q8", "Station 2 · "+WHATM, "External oblique",
   ["External oblique","Internal oblique","Transverse abdominis","Rectus abdominis"]),
 q("s3","Q9", "Station 3 · "+WHATM2, "Orbicularis oculi",
   ["Orbicularis oculi","Orbicularis oris","Temporalis","Buccinator","Masseter"]),
 q("s3","Q10","Station 3 · "+WHATM2, "Zygomaticus major",
   ["Zygomaticus major","Mentalis","Risorius","Zygomaticus minor","Depressor anguli oris"]),
 q("s4","Q11","Station 4 · "+WHATM, "Biceps brachii (long head)",
   ["Coracobrachialis","Biceps brachii (long head)","Biceps brachii (short head)","Supraspinatus","Subscapularis"]),
 q("s4","Q12","Station 4 · "+WHATM, "Flexor digitorum superficialis",
   ["Flexor carpi ulnaris","Flexor digitorum superficialis","Flexor digitorum profundus","Abductor pollicis longus"]),
 q("s4","Q13","Station 4 · "+WHATM2, "Extensor digitorum",
   ["Supinator","Extensor digiti minimi","Extensor carpi radialis longus","Extensor carpi radialis brevis","Extensor digitorum"]),
 q("s4","Q14","Station 4 · "+WHATM2, "Brachioradialis",
   ["Pronator teres","Brachioradialis","Anconeus","Teres major","Teres minor"]),
 q("s5","Q15","Station 5 · "+WHATM2, "Latissimus dorsi",
   ["Latissimus dorsi","Rectus abdominis","Deltoid","Sternocleidomastoid","Serratus anterior"]),
 q("s5","Q16","Station 5 · "+WHATM2, "Rhomboid major",
   ["Iliacus","Psoas major","Diaphragm","Rhomboid major","Rhomboid minor"]),
 q("s5","Q17","Station 5 · What is this muscle's PRIMARY ACTION?", "Extends, adducts and medially rotates arm",
   ["Flexes vertebral column, compresses abdomen","Protracts and depresses scapula",
    "Extends, adducts and medially rotates arm","Flexes neck, rotates head to the opposite side"]),
 q("s5","Q18","Station 5 · What is this muscle's INSERTION?", "Intertubercular sulcus of the humerus",
   ["Intertubercular sulcus of the humerus","Coracoid process of the scapula",
    "Spinous process of the lower vertebrae, iliac crest","Ribs 3 - 5"]),
 q("s6","Q19","Station 6 · "+WHATN, "Tendinous Intersections",
   ["Linea Alba","Anterior Rectus Sheath","Tendinous Intersections","Galea aponeurotica"]),
 q("s6","Q20","Station 6 · "+WHATN, "Iliotibial (IT) Band",
   ["Patellar ligament","Sciatic nerve","Calcaneal tendon","Iliotibial (IT) Band","Quadriceps tendon"]),
 q("s7","Q21","Station 7 · "+WHATS, "Myofibrils",
   ["Myofibrils","Muscle fiber","Endoplasmic reticulum","T-Tubules"]),
 q("s7","Q22","Station 7 · "+WHATS, "Sarcolemma",
   ["Sarcomere","Sarcolemma","Nucleus","Sarcoplasm"]),
]

section = {"id":"inclass","title":"In-Class Prep Quiz","updated":True,
           "excludeFromGlobal":True,"questions":questions}

# ---- load ORIGINAL dataset (pre-inclass backup), append section ----
# Read from the clean backup so existing banks keep their original images/labels;
# we only add the new bank (no swaps into existing banks).
ds  = os.path.join(ROOT,"dataset.js")
src = os.path.join(ROOT,"images/_backups/dataset.before_inclass.js")
txt = open(src, encoding="utf-8").read()
i,j = txt.index("{"), txt.rindex("}")+1
data = json.loads(txt[i:j])

def find(secid, answer):
    for s in data["sections"]:
        if s["id"]==secid:
            for qq in s["questions"]:
                if qq["answer"]==answer: return qq
    return None

# No swaps into existing banks — these photos live only in the new bank.
SWAPS = []
for secid,ans,st,tag in SWAPS:
    qq = find(secid,ans)
    fn,w,h = saved[st]
    if qq is None: print("  SWAP MISS",secid,ans); continue
    qq["image"]="images/"+fn; qq["width_px"]=w; qq["height_px"]=h
    qq["bbox_px"]=pinpx[(st,tag)]
    print("  swapped",secid,"/",ans,"->",fn)

# remove any prior inclass section, then append
data["sections"]=[s for s in data["sections"] if s["id"]!="inclass"]
data["sections"].append(section)

open(ds,"w",encoding="utf-8").write("window.MUSCLE_DATA = "+json.dumps(data,indent=1,ensure_ascii=False)+";\n")
print("dataset.js written. sections:",[s['id'] for s in data['sections']])
