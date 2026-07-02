import cv2

def blur(frame):
    return cv2.GaussianBlur(frame, (31, 31), 0)