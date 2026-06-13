# Muscle Lab Practical — Pin Quiz

Identify-the-pin study app for Week 8 muscles, same style as the bones lab-practical prep:
a red box pins one muscle on the image and you name it — **multiple choice** (1 correct + 5
distractors) or **flashcards**. Filter by region. Runs straight from `index.html` (no server).

## Use it
Open `index.html`, pick regions, choose MCQ or flashcards, **Start session**.

## Fixing pins
If a pin sits on the wrong spot, hit **✎ Fix pin**, then click the correct spot on the image.
Corrections save on your device (localStorage) immediately, so your studying uses them right away.

## Making corrections permanent (publish)
After fixing pins, the setup screen shows a **⬇ Publish corrected dataset** button. It downloads
a `dataset.js` with your corrections baked in — replace the file in this repo and commit, and the
fixes become permanent and sync to every device / the hosted site.

## Data
`dataset.js` (`window.MUSCLE_DATA`) — sections → questions, each
`{image, width_px, height_px, bbox_px:[x0,y0,x1,y1], answer, view_label_pool}`.
Generated from the marker coordinates in the sibling `muscle-label-quiz` project; images are the
blanked OpenStax/Gray's diagrams.
