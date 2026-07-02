import cv2


class BlurEffect:

    def __init__(self):

        # opacity blur
        self.alpha = 0.0

        # kecepatan animasi
        self.speed = 0.04

    def update(self, gesture):

        if gesture == "Victory":

            self.alpha = min(
                self.alpha + self.speed,
                1.0
            )

        else:

            self.alpha = max(
                self.alpha - self.speed,
                0.0
            )

    def apply(self, frame):

        if self.alpha <= 0:
            return frame

        blurred = cv2.GaussianBlur(
            frame,
            (41,41),
            0
        )

        output = cv2.addWeighted(

            blurred,

            self.alpha,

            frame,

            1-self.alpha,

            0

        )

        return output