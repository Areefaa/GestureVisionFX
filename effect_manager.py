import time
import cv2


class EffectManager:

    def __init__(self):

        self.alpha = 0.0
        self.speed = 0.0001

        self.start_time = None
        self.active = False

        self.hold_time = 0.01

    def update(self, gesture):

        if gesture == "Victory":

            if self.start_time is None:
                self.start_time = time.time()

            elapsed = time.time() - self.start_time

            if elapsed >= self.hold_time:
                self.active = True

        else:

            self.start_time = None
            self.active = False

        if self.active:

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

    def progress(self):

        if self.start_time is None:
            return 0

        elapsed = time.time() - self.start_time

        value = elapsed / self.hold_time

        return min(value,1.0)