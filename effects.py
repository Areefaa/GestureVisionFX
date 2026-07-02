import cv2


class BlurEffect:

    def __init__(self):

        self.alpha = 0.0

        self.speed = 0.04

    def update(self, blur_active):

        if blur_active:

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

        return cv2.addWeighted(
            blurred,
            self.alpha,
            frame,
            1-self.alpha,
            0
        )