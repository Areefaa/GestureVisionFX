import cv2

from detector import GestureDetector
from effects import BlurEffect
from gesture_hold import GestureHold
from ui import UI

MODEL_PATH = "assets/models/gesture_recognizer.task"

detector = GestureDetector(MODEL_PATH)

effect = BlurEffect()

hold = GestureHold(hold_time=1.0)

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

    hold.update(gesture)

    effect.update(hold.active)

    frame = effect.apply(frame)

    frame = ui.draw(frame, gesture)

    percent = int(hold.progress() * 100)

    cv2.putText(
        frame,
        f"Hold : {percent}%",
        (20,80),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (255,255,255),
        2
    )

    bar_width = 250

    filled = int(bar_width * hold.progress())

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

    if hold.active:
        status = "Blur Activated"

    elif gesture == "Victory":
        status = "Hold Gesture..."

    else:
        status = "Waiting..."

    cv2.putText(
        frame,
        status,
        (20,150),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.7,
        (0,255,255),
        2
    )

    cv2.imshow("GestureVisionFX", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()