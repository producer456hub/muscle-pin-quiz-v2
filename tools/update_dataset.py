"""Reusable dataset editor. Loads dataset.js, applies per-image dimension
changes and per-(image,answer) bbox changes, writes back in the SAME format
the app's Publish button uses (window.MUSCLE_DATA = <json indent=1>;).

Edit the CONFIG below, then run: python tools/update_dataset.py
"""
import json, re, sys, os

DS = os.path.join(os.path.dirname(__file__), "..", "dataset.js")

# image filename (basename) -> (width_px, height_px)
DIMS = {
    "forearm_ant_blank.png": (658, 980),
    "arm_ant_blank.png": (760, 779),
    "forearm_post_blank.png": (745, 480),
    "arm_post_blank.png": (600, 1504),
    "thigh_ant_blank.png": (372, 2115),
    "leg_post_blank.png": (360, 892),
    "neck_lateral_blank.png": (365, 595),
    "leg_ant_blank.png": (265, 725),
    "girdle_post_blank.png": (660, 465),
    "rotatorcuff_blank.png": (738, 888),
    "diaphragm_blank.png": (1100, 978),
    "intercostals_blank.png": (868, 560),
    "eye_anterior_blank.png": (585, 730),
    "thigh_post_blank.png": (405, 890),
    "abdomen_superficial.png": (960, 720),
    "abdomen_internal_oblique.png": (960, 720),
    "abdomen_rectus_sheath.png": (960, 720),
    "abdomen_ct.jpg": (771, 943),
    "abdomen_transversus.png": (402, 700),
    "tissue_blank.png": (801, 642),
    "facial_anterior_blank.png": (658, 1090),
    "Lateral_head_anatomy.jpg": (1205, 1424),
}
# (image basename, answer) -> [cx, cy] center  (auto-expanded to a 30px box)
CENTERS = {
    ("forearm_ant_blank.png", "Pronator teres"): [450, 300],
    ("forearm_ant_blank.png", "Brachioradialis"): [235, 335],
    ("forearm_ant_blank.png", "Flexor carpi radialis"): [300, 470],
    ("forearm_ant_blank.png", "Palmaris longus"): [378, 478],
    ("forearm_ant_blank.png", "Flexor carpi ulnaris"): [428, 678],
    ("forearm_ant_blank.png", "Flexor digitorum superficialis"): [340, 658],

    ("arm_ant_blank.png", "Biceps brachii (short head)"): [500, 325],
    ("arm_ant_blank.png", "Biceps brachii (long head)"): [578, 365],
    ("arm_ant_blank.png", "Brachialis"): [625, 688],

    ("forearm_post_blank.png", "Anconeus"): [650, 55],
    ("forearm_post_blank.png", "Brachioradialis"): [585, 52],
    ("forearm_post_blank.png", "Extensor carpi radialis longus"): [548, 92],
    ("forearm_post_blank.png", "Extensor carpi radialis brevis"): [505, 128],
    ("forearm_post_blank.png", "Extensor digitorum"): [435, 180],
    ("forearm_post_blank.png", "Extensor digiti minimi"): [458, 223],
    ("forearm_post_blank.png", "Extensor carpi ulnaris"): [518, 250],
    ("forearm_post_blank.png", "Abductor pollicis longus"): [335, 305],

    ("arm_post_blank.png", "Triceps brachii (lateral head)"): [190, 825],
    ("arm_post_blank.png", "Triceps brachii (long head)"): [333, 906],
    ("arm_post_blank.png", "Triceps brachii (medial head)"): [333, 1377],

    ("thigh_ant_blank.png", "Psoas major"): [218, 330],
    ("thigh_ant_blank.png", "Iliacus"): [180, 360],
    ("thigh_ant_blank.png", "Tensor fasciae latae"): [160, 255],
    ("thigh_ant_blank.png", "Rectus femoris"): [205, 590],
    ("thigh_ant_blank.png", "Vastus lateralis"): [180, 720],
    ("thigh_ant_blank.png", "Vastus medialis"): [305, 1375],
    ("thigh_ant_blank.png", "Sartorius"): [215, 900],
    ("thigh_ant_blank.png", "Adductor longus"): [238, 485],
    ("thigh_ant_blank.png", "Adductor magnus"): [252, 625],
    ("thigh_ant_blank.png", "Gracilis"): [260, 560],
    ("thigh_ant_blank.png", "Quadriceps tendon"): [320, 1690],
    ("thigh_ant_blank.png", "Patellar ligament"): [325, 1985],

    ("leg_post_blank.png", "Gastrocnemius"): [150, 215],
    ("leg_post_blank.png", "Soleus"): [90, 440],
    ("leg_post_blank.png", "Calcaneal (Achilles) tendon"): [100, 650],

    ("neck_lateral_blank.png", "Sternocleidomastoid"): [145, 330],
    ("neck_lateral_blank.png", "Trapezius"): [295, 360],

    ("leg_ant_blank.png", "Tibialis anterior"): [118, 200],
    ("leg_ant_blank.png", "Extensor digitorum longus"): [72, 250],
    ("leg_ant_blank.png", "Extensor hallucis longus"): [82, 385],
    ("leg_ant_blank.png", "Fibularis longus"): [46, 270],

    ("girdle_post_blank.png", "Trapezius"): [205, 205],
    ("girdle_post_blank.png", "Deltoid"): [78, 215],
    ("girdle_post_blank.png", "Rhomboid minor"): [415, 190],
    ("girdle_post_blank.png", "Rhomboid major"): [408, 228],

    ("rotatorcuff_blank.png", "Supraspinatus"): [560, 70],
    ("rotatorcuff_blank.png", "Infraspinatus"): [660, 250],
    ("rotatorcuff_blank.png", "Teres minor"): [515, 245],
    ("rotatorcuff_blank.png", "Teres major"): [540, 335],
    ("rotatorcuff_blank.png", "Deltoid"): [690, 165],

    ("diaphragm_blank.png", "Diaphragm"): [936, 555],
    ("diaphragm_blank.png", "Central tendon"): [527, 258],

    ("intercostals_blank.png", "External intercostals"): [150, 205],
    ("intercostals_blank.png", "Internal intercostals"): [665, 330],

    ("eye_anterior_blank.png", "Superior Rectus"): [255, 165],
    ("eye_anterior_blank.png", "Inferior Rectus"): [250, 510],
    ("eye_anterior_blank.png", "Lateral Rectus"): [95, 360],
    ("eye_anterior_blank.png", "Medial Rectus"): [470, 360],
    ("eye_anterior_blank.png", "Superior Oblique"): [490, 68],
    ("eye_anterior_blank.png", "Inferior Oblique"): [330, 660],

    ("thigh_post_blank.png", "Gluteus maximus"): [208, 242],
    ("thigh_post_blank.png", "Gluteus medius"): [300, 95],
    ("thigh_post_blank.png", "Piriformis"): [296, 172],
    ("thigh_post_blank.png", "Biceps femoris"): [316, 478],
    ("thigh_post_blank.png", "Semimembranosus"): [236, 520],
    ("thigh_post_blank.png", "Semitendinosus"): [192, 575],

    ("abdomen_superficial.png", "Pectoralis major"): [300, 110],
    ("abdomen_superficial.png", "Latissimus dorsi"): [665, 100],
    ("abdomen_superficial.png", "Serratus anterior"): [560, 150],
    ("abdomen_superficial.png", "External oblique"): [500, 470],
    ("abdomen_internal_oblique.png", "Internal oblique"): [175, 480],
    ("abdomen_rectus_sheath.png", "Anterior rectus sheath"): [230, 430],
    ("abdomen_ct.jpg", "Rectus abdominis"): [300, 430],
    ("abdomen_ct.jpg", "Linea alba"): [392, 290],
    ("abdomen_ct.jpg", "Tendinous intersections"): [322, 345],
    ("abdomen_transversus.png", "Transverse abdominis"): [120, 400],

    ("tissue_blank.png", "Skeletal Muscle Fiber"): [170, 100],
    ("tissue_blank.png", "Nucleus"): [140, 158],
    ("tissue_blank.png", "Mitochondria"): [265, 70],
    ("tissue_blank.png", "Sarcolemma"): [205, 48],
    ("tissue_blank.png", "Myofibrils"): [280, 455],
    ("tissue_blank.png", "Sarcoplasm"): [225, 512],
    ("tissue_blank.png", "Sarcomere"): [405, 490],
    ("tissue_blank.png", "Sarcoplasmic reticulum"): [95, 490],

    ("facial_anterior_blank.png", "Galea aponeurotica"): [330, 72],
    ("facial_anterior_blank.png", "Frontalis"): [425, 265],
    ("facial_anterior_blank.png", "Orbicularis oculi"): [548, 480],
    ("facial_anterior_blank.png", "Nasalis"): [312, 540],
    ("facial_anterior_blank.png", "Zygomaticus minor"): [492, 690],
    ("facial_anterior_blank.png", "Zygomaticus major"): [520, 765],
    ("facial_anterior_blank.png", "Orbicularis oris"): [360, 895],
    ("facial_anterior_blank.png", "Buccinator"): [490, 862],
    ("facial_anterior_blank.png", "Risorius"): [528, 838],
    ("facial_anterior_blank.png", "Depressor anguli oris"): [455, 925],
    ("facial_anterior_blank.png", "Mentalis"): [345, 985],

    ("Lateral_head_anatomy.jpg", "Temporalis"): [400, 400],
    ("Lateral_head_anatomy.jpg", "Masseter"): [410, 905],
    ("Lateral_head_anatomy.jpg", "Occipitalis"): [975, 620],
    ("Lateral_head_anatomy.jpg", "Frontalis"): [290, 360],
    ("Lateral_head_anatomy.jpg", "Orbicularis oculi"): [165, 470],
    ("Lateral_head_anatomy.jpg", "Zygomaticus major"): [235, 660],
    ("Lateral_head_anatomy.jpg", "Sternocleidomastoid"): [650, 1080],
    ("Lateral_head_anatomy.jpg", "Trapezius"): [880, 1000],
}
H = 15  # half box size
PINS = {k: [v[0]-H, v[1]-H, v[0]+H, v[1]+H] for k, v in CENTERS.items()}

def main():
    raw = open(DS, encoding="utf-8").read()
    m = re.search(r"window\.MUSCLE_DATA\s*=\s*", raw)
    start = m.end()
    end = raw.rfind("}") + 1
    data = json.loads(raw[start:end])
    nd = np = 0
    for s in data["sections"]:
        for q in s["questions"]:
            base = q["image"].split("/")[-1]
            if base in DIMS:
                q["width_px"], q["height_px"] = DIMS[base]
                nd += 1
            key = (base, q["answer"])
            if key in PINS:
                q["bbox_px"] = PINS[key]
                np += 1
    out = "window.MUSCLE_DATA = " + json.dumps(data, indent=1) + ";\n"
    open(DS, "w", encoding="utf-8").write(out)
    print(f"updated dims on {nd} questions, pins on {np} questions")
    missing = [k for k in PINS if not any(
        (q["image"].split("/")[-1], q["answer"]) == k
        for s in data["sections"] for q in s["questions"])]
    if missing:
        print("WARNING unmatched pins:", missing)

main()
