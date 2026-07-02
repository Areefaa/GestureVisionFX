import cv2
import numpy as np
import time


class BlurEffect:

    def __init__(self):

        self.alpha = 0.0

        self.fade_in_speed = 0.12
        self.fade_out_speed = 0.06

        # Flash
        self.flash = False
        self.flash_start = 0
        self.flash_duration = 0.12

    def trigger_flash(self):

        self.flash = True
        self.flash_start = time.time()

    def update(self, blur_active):

        if blur_active:

            self.alpha = min(
                self.alpha + self.fade_in_speed,
                1.0
            )

        else:

            self.alpha = max(
                self.alpha - self.fade_out_speed,
                0.0
            )

    def apply(self, frame):

        output = frame.copy()

        # Blur
        if self.alpha > 0:

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

        # Flash
        if self.flash:

            elapsed = time.time() - self.flash_start

            if elapsed <= self.flash_duration:

                white = np.full_like(output,255)

                strength = 1 - elapsed/self.flash_duration

                output = cv2.addWeighted(
                    white,
                    strength,
                    output,
                    1-strength,
                    0
                )

            else:

                self.flash = False

        return output