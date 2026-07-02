import cv2

from detector import GestureDetector
from effects import BlurEffect
from countdown import Countdown
from ui import UI

MODEL_PATH = "assets/models/gesture_recognizer.task"

detector = GestureDetector(MODEL_PATH)
effect = BlurEffect()
countdown = Countdown(duration=1.0)
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

    # ==========================
    # Gesture Detection
    # ==========================

    gesture = detector.detect(frame)

    # ==========================
    # Countdown Logic
    # ==========================

    if gesture == "Victory":

        countdown.start()

    else:

        countdown.reset()

    number = countdown.update()

    # ==========================
    # Blur
    # ==========================

    effect.update(countdown.finished)

    frame = effect.apply(frame)

    # ==========================
    # UI
    # ==========================

    frame = ui.draw(frame, gesture)

    # ==========================
    # Status
    # ==========================

    if countdown.finished:

        status = "Blur Activated"

    elif countdown.running():

        status = "Countdown..."

    elif gesture == "Victory":

        status = "Starting..."

    else:

        status = "Waiting..."

    cv2.putText(
        frame,
        status,
        (20,40),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (0,255,255),
        2
    )

    # ==========================
    # Countdown Number
    # ==========================

    if countdown.running():

        overlay = frame.copy()

        cv2.putText(
            overlay,
            str(number),
            (
                frame.shape[1]//2-40,
                frame.shape[0]//2+30
            ),
            cv2.FONT_HERSHEY_DUPLEX,
            5,
            (255,255,255),
            8
        )

        frame = cv2.addWeighted(
            overlay,
            0.8,
            frame,
            0.2,
            0
        )

    cv2.imshow("GestureVisionFX", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()