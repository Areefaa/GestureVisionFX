import cv2
from effects import blur
from utils import draw_text

cap = cv2.VideoCapture(0)

blur_on = False

while True:
    ret, frame = cap.read()

    if not ret:
        break

    frame = cv2.flip(frame, 1)

    if blur_on:
        frame = blur(frame)
        draw_text(frame, "BLUR MODE")
    else:
        draw_text(frame, "NORMAL MODE")

    cv2.imshow("GestureVisionFX", frame)

    key = cv2.waitKey(1) & 0xFF

    if key == ord("b"):
        blur_on = not blur_on

    if key == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()