import cv2

from detector import GestureDetector
from effects import blur
from ui import draw

MODEL_PATH = "assets/models/gesture_recognizer.task"

detector = GestureDetector(MODEL_PATH)

cap = cv2.VideoCapture(0)

while True:

    ret, frame = cap.read()

    if not ret:
        break

    frame = cv2.flip(frame,1)

    gesture = detector.detect(frame)

    if gesture == "Victory":
        frame = blur(frame)

    draw(frame, gesture)

    cv2.imshow("GestureVisionFX", frame)

    key = cv2.waitKey(1)

    if key == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()