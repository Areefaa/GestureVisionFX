import cv2

class EffectManager:

    def __init__(self):
        self.blur_strength = 0

    def update(self, gesture):

        if gesture == "Victory":
            self.blur_strength = min(self.blur_strength + 3, 41)

        else:
            self.blur_strength = max(self.blur_strength - 3, 0)

    def apply(self, frame):

        if self.blur_strength < 3:
            return frame

        k = self.blur_strength

        if k % 2 == 0:
            k += 1

        return cv2.GaussianBlur(frame, (k, k), 0)