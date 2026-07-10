import cv2
import os
from datetime import datetime

from detector import GestureDetector
from effects import BlurEffect
from countdown import Countdown
from ui import UI

MODEL_PATH = "assets/models/gesture_recognizer.task"

# ======================================
# Initialize
# ======================================

detector = GestureDetector(MODEL_PATH)
effect = BlurEffect()
countdown = Countdown(duration=1.0)
ui = UI()

flash_triggered = False
capture_saved = False

CAPTURE_DIR = "captures"
os.makedirs(CAPTURE_DIR, exist_ok=True)

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Cannot open webcam")
    exit()

# ======================================
# Main Loop
# ======================================

while True:

    ret, frame = cap.read()

    if not ret:
        break

    frame = cv2.flip(frame, 1)

    # Simpan frame asli (tanpa blur & UI)
    clean_frame = frame.copy()

    # ==============================
    # Gesture Detection
    # ==============================

    gesture = detector.detect(frame)

    # ==============================
    # Countdown
    # ==============================

    if gesture == "Victory":
        countdown.start()
    else:
        countdown.reset()

    number = countdown.update()

    # ==============================
    # Trigger Flash
    # ==============================

    if countdown.finished and not flash_triggered:

        effect.trigger_flash()

        flash_triggered = True

    # ==============================
    # Save Screenshot
    # ==============================

    if countdown.finished and not capture_saved:

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

        filename = os.path.join(
            CAPTURE_DIR,
            f"capture_{timestamp}.jpg"
        )

        cv2.imwrite(filename, clean_frame)

        print(f"[Saved] {filename}")

        capture_saved = True

    # ==============================
    # Reset
    # ==============================

    if not countdown.finished:

        flash_triggered = False
        capture_saved = False

    # ==============================
    # Effects
    # ==============================

    effect.update(countdown.finished)

    frame = effect.apply(frame)

    # ==============================
    # UI
    # ==============================

    frame = ui.draw(frame, gesture)

    # ==============================
    # Status
    # ==============================

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
        (20, 80),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (0, 255, 255),
        2
    )

    # ==============================
    # Countdown Number
    # ==============================

    if countdown.running():

        scale = 1.5 + countdown.scale()

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

        # Outline Hitam
        cv2.putText(
            overlay,
            text,
            (x, y),
            font,
            scale,
            (0, 0, 0),
            thickness + 6
        )

        # Isi Putih
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

    # ==============================
    # Saved Indicator
    # ==============================

    if capture_saved:

        cv2.putText(
            frame,
            "Screenshot Saved!",
            (20, 120),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            (0, 255, 0),
            2
        )

    # ==============================
    # Show
    # ==============================

    cv2.imshow("GestureVisionFX", frame)

    key = cv2.waitKey(1) & 0xFF

    if key == ord("q"):
        break

# ======================================
# Cleanup
# ======================================

cap.release()
cv2.destroyAllWindows()