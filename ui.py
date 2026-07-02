import cv2


def draw(frame, gesture):

    text = gesture if gesture else "No Gesture"

    cv2.putText(
        frame,
        text,
        (20,40),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0,255,0),
        2
    )