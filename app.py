import cv2

from detector import GestureDetector
from effects import BlurEffect
from ui import UI

MODEL_PATH = "assets/models/gesture_recognizer.task"

detector = GestureDetector(MODEL_PATH)
effect = BlurEffect()
ui = UI()

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Cannot open webcam")
    exit()

while True:

    ret, frame = cap.read()

    if not ret:
        break

    frame = cv2.flip(frame, 1)

    gesture = detector.detect(frame)

    effect.update(gesture)

    frame = effect.apply(frame)

    frame = ui.draw(frame, gesture)

    percent = int(effect.alpha * 100)

    cv2.putText(
        frame,
        f"Blur : {percent}%",
        (20,80),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (255,255,255),
        2
    )

    bar_width = 250

    filled = int(bar_width * percent / 100)

    cv2.rectangle(
        frame,
        (20,100),
        (20+bar_width,120),
        (120,120,120),
        2
    )

    cv2.rectangle(
        frame,
        (20,100),
        (20+filled,120),
        (255,255,255),
        -1
    )

    cv2.imshow("GestureVisionFX", frame)

    key = cv2.waitKey(1)

    if key == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()