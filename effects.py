import cv2


def blur(frame):

    return cv2.GaussianBlur(
        frame,
        (41,41),
        0
    )