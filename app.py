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

flash_triggered = False

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

    if gesture == "Victory":
        countdown.start()
    else:
        countdown.reset()

    number = countdown.update()

    if countdown.finished and not flash_triggered:
        effect.trigger_flash()
        flash_triggered = True

    if not countdown.finished:
        flash_triggered = False

    effect.update(countdown.finished)

    frame = effect.apply(frame)

    frame = ui.draw(frame, gesture)

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
        (20, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (0, 255, 255),
        2
    )


    if countdown.running():

        scale = countdown.scale()

        text = str(number)

        font = cv2.FONT_HERSHEY_DUPLEX

        thickness = 8

        (w, h), _ = cv2.getTextSize(
            text,
            font,
            scale,
            thickness
        )

        x = (frame.shape[1] - w) // 2
        y = (frame.shape[0] + h) // 2

        overlay = frame.copy()

        cv2.putText(
            overlay,
            text,
            (x, y),
            font,
            scale,
            (255, 255, 255),
            thickness
        )

        frame = cv2.addWeighted(
            overlay,
            0.9,
            frame,
            0.1,
            0
        )

    cv2.imshow("GestureVisionFX", frame)

    key = cv2.waitKey(1) & 0xFF

    if key == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()