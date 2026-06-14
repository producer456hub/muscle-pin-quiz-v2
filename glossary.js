// Glossary of every term studied across the project, grouped by category.
// `alt` lists alternate spellings/casing found in dataset.js so coverage matches.
window.GLOSSARY = {
 categories: [
  "Muscle Cell & Tissue","Face & Scalp","Mastication (chewing)","Neck",
  "Extraocular (Eye)","Thorax & Abdomen","Shoulder & Scapula","Arm",
  "Forearm & Hand","Hip & Thigh","Leg & Foot","Connective / Non-muscular"
 ],
 terms: [
  // ---- Muscle Cell & Tissue ----
  {c:"Muscle Cell & Tissue", t:"Skeletal Muscle Fiber", d:"A single long, multinucleated muscle cell — the basic structural unit of skeletal muscle."},
  {c:"Muscle Cell & Tissue", t:"Muscle fiber", d:"Another name for a single skeletal muscle cell."},
  {c:"Muscle Cell & Tissue", t:"Myofibrils", d:"Rod-like contractile bundles of actin and myosin that fill the fiber and shorten to produce contraction."},
  {c:"Muscle Cell & Tissue", t:"Sarcomere", d:"The repeating Z-disc-to-Z-disc segment of a myofibril; the functional (contractile) unit of muscle."},
  {c:"Muscle Cell & Tissue", t:"Sarcolemma", d:"The plasma membrane of a muscle fiber."},
  {c:"Muscle Cell & Tissue", t:"Sarcoplasm", d:"The cytoplasm of a muscle fiber."},
  {c:"Muscle Cell & Tissue", t:"Sarcoplasmic reticulum", d:"Specialized smooth ER that stores and releases the calcium that triggers contraction."},
  {c:"Muscle Cell & Tissue", t:"T-Tubules", d:"Inward folds of the sarcolemma that carry the action potential deep into the fiber."},
  {c:"Muscle Cell & Tissue", t:"Nucleus", d:"Organelle holding the cell's DNA; skeletal fibers have many, pushed to the periphery."},
  {c:"Muscle Cell & Tissue", t:"Mitochondria", d:"Organelles that make ATP by aerobic respiration to power contraction."},
  {c:"Muscle Cell & Tissue", t:"Endoplasmic reticulum", d:"Membrane network for protein/lipid synthesis; in muscle it is specialized as the sarcoplasmic reticulum."},

  // ---- Face & Scalp ----
  {c:"Face & Scalp", t:"Frontalis", d:"Raises the eyebrows and wrinkles the forehead (frontal belly of occipitofrontalis)."},
  {c:"Face & Scalp", t:"Occipitalis", d:"Pulls the scalp backward (occipital belly of occipitofrontalis)."},
  {c:"Face & Scalp", t:"Orbicularis oculi", d:"Sphincter around the eye; closes the eyelids (blinking, squinting)."},
  {c:"Face & Scalp", t:"Orbicularis oris", d:"Sphincter of the mouth; closes and purses the lips."},
  {c:"Face & Scalp", t:"Zygomaticus major", d:"Draws the corner of the mouth up and back — smiling."},
  {c:"Face & Scalp", t:"Zygomaticus minor", d:"Elevates the upper lip."},
  {c:"Face & Scalp", t:"Risorius", d:"Pulls the corner of the mouth sideways (grimace)."},
  {c:"Face & Scalp", t:"Buccinator", d:"Compresses the cheek against the teeth; aids chewing, blowing, and sucking."},
  {c:"Face & Scalp", t:"Mentalis", d:"Protrudes the lower lip and wrinkles the chin."},
  {c:"Face & Scalp", t:"Depressor anguli oris", d:"Pulls the corner of the mouth downward — frowning."},
  {c:"Face & Scalp", t:"Nasalis", d:"Compresses and flares the nostrils."},

  // ---- Mastication ----
  {c:"Mastication (chewing)", t:"Temporalis", d:"Elevates and retracts the mandible; a major chewing muscle (fan-shaped, over the temple)."},
  {c:"Mastication (chewing)", t:"Masseter", d:"Elevates the mandible — the strongest chewing muscle (over the angle of the jaw)."},

  // ---- Neck ----
  {c:"Neck", t:"Sternocleidomastoid", d:"Together flex the neck; one side alone rotates the head to the opposite side."},
  {c:"Neck", t:"Trapezius", d:"Elevates, retracts, and depresses the scapula; extends the head/neck."},
  {c:"Neck", t:"Splenius", d:"Extends and rotates the head and neck (splenius capitis/cervicis)."},
  {c:"Neck", t:"Levator scapulae", d:"Elevates the scapula and tilts its socket downward."},
  {c:"Neck", t:"Anterior scalene", d:"Elevates the first rib; flexes and laterally bends the neck."},
  {c:"Neck", t:"Medial scalene", d:"Elevates the first rib; laterally flexes the neck."},

  // ---- Extraocular ----
  {c:"Extraocular (Eye)", t:"Superior Rectus", d:"Elevates the eye (also adducts and medially rotates it)."},
  {c:"Extraocular (Eye)", t:"Inferior Rectus", d:"Depresses the eye (also adducts and laterally rotates it)."},
  {c:"Extraocular (Eye)", t:"Medial Rectus", d:"Adducts the eye — turns the pupil toward the nose."},
  {c:"Extraocular (Eye)", t:"Lateral Rectus", d:"Abducts the eye — turns the pupil outward."},
  {c:"Extraocular (Eye)", t:"Superior Oblique", d:"Depresses, abducts, and medially rotates the eye (runs through the trochlea)."},
  {c:"Extraocular (Eye)", t:"Inferior Oblique", d:"Elevates, abducts, and laterally rotates the eye."},

  // ---- Thorax & Abdomen ----
  {c:"Thorax & Abdomen", t:"Pectoralis major", d:"Flexes, adducts, and medially rotates the arm at the shoulder (large chest fan)."},
  {c:"Thorax & Abdomen", t:"Pectoralis minor", d:"Protracts and depresses the scapula; elevates the ribs (deep to pec major)."},
  {c:"Thorax & Abdomen", t:"Serratus anterior", d:"Protracts and upwardly rotates the scapula, holding it to the chest wall (\"boxer's muscle\")."},
  {c:"Thorax & Abdomen", t:"External oblique", d:"Most superficial side ab; flexes/rotates the trunk and compresses the abdomen (fibers point \"hands in pockets\")."},
  {c:"Thorax & Abdomen", t:"Internal oblique", d:"Middle side ab; flexes/rotates the trunk and compresses the abdomen (fibers run opposite the external oblique)."},
  {c:"Thorax & Abdomen", t:"Transverse abdominis", d:"Deepest ab muscle; horizontal fibers compress the abdomen like a corset."},
  {c:"Thorax & Abdomen", t:"Rectus abdominis", d:"Flexes the vertebral column and compresses the abdomen (the \"six-pack\")."},
  {c:"Thorax & Abdomen", t:"External intercostals", d:"Elevate the ribs during inspiration (breathing in).", alt:["External intercostal"]},
  {c:"Thorax & Abdomen", t:"Internal intercostals", d:"Depress the ribs during forced expiration (breathing out).", alt:["Internal intercostal"]},
  {c:"Thorax & Abdomen", t:"Innermost intercostals", d:"Deepest intercostal layer; assist the internal intercostals.", alt:["Innermost intercostal"]},
  {c:"Thorax & Abdomen", t:"Diaphragm", d:"Primary breathing muscle; the dome flattens to pull air into the lungs."},
  {c:"Thorax & Abdomen", t:"Quadratus lumborum", d:"Extends and laterally flexes the lumbar spine; depresses the 12th rib."},
  {c:"Thorax & Abdomen", t:"Psoas major", d:"Powerful hip flexor (also flexes the trunk); joins iliacus as the iliopsoas."},

  // ---- Shoulder & Scapula ----
  {c:"Shoulder & Scapula", t:"Deltoid", d:"Abducts the arm; front fibers flex/medially rotate, back fibers extend/laterally rotate."},
  {c:"Shoulder & Scapula", t:"Supraspinatus", d:"Starts arm abduction (first ~15°); rotator cuff."},
  {c:"Shoulder & Scapula", t:"Infraspinatus", d:"Laterally (externally) rotates the arm; rotator cuff."},
  {c:"Shoulder & Scapula", t:"Teres minor", d:"Laterally rotates and adducts the arm; rotator cuff."},
  {c:"Shoulder & Scapula", t:"Teres major", d:"Adducts and medially rotates the arm (\"lat's little helper\")."},
  {c:"Shoulder & Scapula", t:"Subscapularis", d:"Medially (internally) rotates the arm; rotator cuff (on the front of the scapula)."},
  {c:"Shoulder & Scapula", t:"Rhomboid major", d:"Retracts and stabilizes the scapula (pulls shoulder blades together)."},
  {c:"Shoulder & Scapula", t:"Rhomboid minor", d:"Retracts and stabilizes the scapula (just above rhomboid major)."},
  {c:"Shoulder & Scapula", t:"Latissimus dorsi", d:"Extends, adducts, and medially rotates the arm; inserts in the intertubercular groove of the humerus."},

  // ---- Arm ----
  {c:"Arm", t:"Biceps brachii", d:"Flexes the elbow and supinates the forearm."},
  {c:"Arm", t:"Biceps brachii (long head)", d:"Lateral head of the biceps; its tendon crosses the shoulder through the intertubercular groove."},
  {c:"Arm", t:"Biceps brachii (short head)", d:"Medial head of the biceps; originates from the coracoid process of the scapula."},
  {c:"Arm", t:"Brachialis", d:"The prime mover of elbow flexion (lies deep to the biceps)."},
  {c:"Arm", t:"Coracobrachialis", d:"Flexes and adducts the arm at the shoulder."},
  {c:"Arm", t:"Triceps brachii", d:"Extends the elbow (the only posterior arm muscle)."},
  {c:"Arm", t:"Triceps brachii (long head)", d:"Crosses the shoulder; extends the elbow and adducts the arm."},
  {c:"Arm", t:"Triceps brachii (lateral head)", d:"Strong elbow extensor on the lateral back of the arm."},
  {c:"Arm", t:"Triceps brachii (medial head)", d:"Deep elbow extensor, active in all elbow extension."},
  {c:"Arm", t:"Anconeus", d:"Assists elbow extension and stabilizes the joint (small, at the elbow)."},

  // ---- Forearm & Hand ----
  {c:"Forearm & Hand", t:"Pronator teres", d:"Pronates the forearm (turns palm down) and helps flex the elbow."},
  {c:"Forearm & Hand", t:"Flexor carpi radialis", d:"Flexes and abducts the wrist (radial flexion)."},
  {c:"Forearm & Hand", t:"Palmaris longus", d:"Flexes the wrist and tenses the palmar fascia (absent in many people)."},
  {c:"Forearm & Hand", t:"Flexor carpi ulnaris", d:"Flexes and adducts the wrist (ulnar flexion)."},
  {c:"Forearm & Hand", t:"Flexor digitorum superficialis", d:"Flexes the middle knuckles (PIP joints) of fingers 2–5."},
  {c:"Forearm & Hand", t:"Flexor digitorum profundus", d:"Flexes the fingertips (DIP joints) of fingers 2–5."},
  {c:"Forearm & Hand", t:"Flexor pollicis longus", d:"Flexes the thumb."},
  {c:"Forearm & Hand", t:"Brachioradialis", d:"Flexes the elbow; strongest with the forearm in mid-position (thumbs-up)."},
  {c:"Forearm & Hand", t:"Extensor carpi radialis longus", d:"Extends and abducts the wrist."},
  {c:"Forearm & Hand", t:"Extensor carpi radialis brevis", d:"Extends and abducts the wrist (shorter, deeper than the longus)."},
  {c:"Forearm & Hand", t:"Extensor digitorum", d:"Extends fingers 2–5 and helps extend the wrist."},
  {c:"Forearm & Hand", t:"Extensor digiti minimi", d:"Extends the little finger."},
  {c:"Forearm & Hand", t:"Extensor carpi ulnaris", d:"Extends and adducts the wrist."},
  {c:"Forearm & Hand", t:"Supinator", d:"Supinates the forearm (turns the palm up); deep around the radius."},
  {c:"Forearm & Hand", t:"Abductor pollicis longus", d:"Abducts and extends the thumb."},
  {c:"Forearm & Hand", t:"Extensor pollicis brevis", d:"Extends the proximal phalanx of the thumb."},

  // ---- Hip & Thigh ----
  {c:"Hip & Thigh", t:"Iliacus", d:"Flexes the thigh at the hip; joins psoas major as the iliopsoas."},
  {c:"Hip & Thigh", t:"Iliopsoas", d:"Psoas major + iliacus combined — the most powerful hip flexor."},
  {c:"Hip & Thigh", t:"Tensor fasciae latae", d:"Flexes and abducts the thigh; tightens the IT band."},
  {c:"Hip & Thigh", t:"Sartorius", d:"Flexes, abducts, and laterally rotates the thigh and flexes the knee (longest muscle in the body)."},
  {c:"Hip & Thigh", t:"Rectus femoris", d:"Quadriceps muscle that extends the knee and flexes the hip."},
  {c:"Hip & Thigh", t:"Vastus lateralis", d:"Quadriceps; extends the knee (lateral thigh)."},
  {c:"Hip & Thigh", t:"Vastus medialis", d:"Quadriceps; extends the knee (medial thigh, the teardrop)."},
  {c:"Hip & Thigh", t:"Vastus intermedius", d:"Quadriceps; extends the knee (deep, between the vasti)."},
  {c:"Hip & Thigh", t:"Adductor longus", d:"Adducts and flexes the thigh."},
  {c:"Hip & Thigh", t:"Adductor magnus", d:"Large adductor of the thigh (also assists flexion and extension)."},
  {c:"Hip & Thigh", t:"Pectineus", d:"Adducts and flexes the thigh."},
  {c:"Hip & Thigh", t:"Gracilis", d:"Adducts the thigh and flexes the knee (thin, most medial thigh muscle)."},
  {c:"Hip & Thigh", t:"Gluteus maximus", d:"Powerful hip extensor; laterally rotates the thigh."},
  {c:"Hip & Thigh", t:"Gluteus medius", d:"Abducts and medially rotates the thigh; steadies the pelvis while walking."},
  {c:"Hip & Thigh", t:"Gluteus minimus", d:"Abducts and medially rotates the thigh (deepest glute)."},
  {c:"Hip & Thigh", t:"Piriformis", d:"Laterally rotates and abducts the flexed thigh."},
  {c:"Hip & Thigh", t:"Obturator externus", d:"Laterally rotates the thigh."},
  {c:"Hip & Thigh", t:"Superior gemellus", d:"Laterally rotates the thigh (with the obturator internus)."},
  {c:"Hip & Thigh", t:"Quadratus femoris", d:"Laterally rotates the thigh (flat, square deep rotator)."},
  {c:"Hip & Thigh", t:"Biceps femoris", d:"Lateral hamstring; flexes the knee and extends the hip."},
  {c:"Hip & Thigh", t:"Semimembranosus", d:"Medial hamstring; flexes the knee and extends the hip."},
  {c:"Hip & Thigh", t:"Semitendinosus", d:"Medial hamstring; flexes the knee and extends the hip."},

  // ---- Leg & Foot ----
  {c:"Leg & Foot", t:"Tibialis anterior", d:"Dorsiflexes and inverts the foot (front of the shin)."},
  {c:"Leg & Foot", t:"Extensor digitorum longus", d:"Extends the toes and dorsiflexes the foot."},
  {c:"Leg & Foot", t:"Extensor hallucis longus", d:"Extends the big toe and dorsiflexes the foot."},
  {c:"Leg & Foot", t:"Fibularis longus", d:"Plantarflexes and everts the foot; supports the arches."},
  {c:"Leg & Foot", t:"Fibularis brevis", d:"Plantarflexes and everts the foot."},
  {c:"Leg & Foot", t:"Gastrocnemius", d:"Plantarflexes the foot and flexes the knee (the calf bulge)."},
  {c:"Leg & Foot", t:"Soleus", d:"Plantarflexes the foot (deep to the gastrocnemius); key for standing."},
  {c:"Leg & Foot", t:"Plantaris", d:"Weakly plantarflexes the foot and flexes the knee (long thin tendon)."},
  {c:"Leg & Foot", t:"Popliteus", d:"\"Unlocks\" the extended knee by medially rotating the tibia."},
  {c:"Leg & Foot", t:"Tibialis posterior", d:"Plantarflexes and inverts the foot; supports the medial arch (deep)."},

  // ---- Connective / Non-muscular ----
  {c:"Connective / Non-muscular", t:"Galea aponeurotica", d:"Flat tendon sheet over the skull connecting the frontalis and occipitalis (epicranial aponeurosis)."},
  {c:"Connective / Non-muscular", t:"Linea alba", d:"Fibrous midline seam of the abdomen where the left and right ab aponeuroses meet.", alt:["Linea Alba"]},
  {c:"Connective / Non-muscular", t:"Tendinous intersections", d:"Fibrous bands crossing the rectus abdominis that divide it into the \"six-pack\" segments.", alt:["Tendinous Intersections"]},
  {c:"Connective / Non-muscular", t:"Anterior rectus sheath", d:"Aponeurotic sheet covering the front of the rectus abdominis.", alt:["Anterior Rectus Sheath"]},
  {c:"Connective / Non-muscular", t:"Central tendon", d:"Flat aponeurotic sheet at the top of the diaphragm where its muscle fibers insert."},
  {c:"Connective / Non-muscular", t:"Quadriceps tendon", d:"Tendon joining the four quadriceps muscles to the patella (kneecap)."},
  {c:"Connective / Non-muscular", t:"Patellar ligament", d:"Continuation of the quad tendon from the patella to the tibial tuberosity."},
  {c:"Connective / Non-muscular", t:"Iliotibial (IT) band", d:"Thick fascial band down the lateral thigh from the iliac crest to the tibia.", alt:["Iliotibial (IT) Band"]},
  {c:"Connective / Non-muscular", t:"Calcaneal (Achilles) tendon", d:"Tendon of the gastrocnemius and soleus that attaches to the heel bone (calcaneus).", alt:["Calcaneal tendon"]},
  {c:"Connective / Non-muscular", t:"Sciatic nerve", d:"The body's largest nerve; runs down the back of the thigh (not a muscle)."}
 ]
};
