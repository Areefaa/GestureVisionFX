import cv2


class BlurEffect:

    def __init__(self):
        self.blur_level = 0          
        self.max_blur = 41           
        self.speed = 2               

    def update(self, gesture):

        if gesture == "Victory":
            self.blur_level = min(
                self.blur_level + self.speed,
                self.max_blur
            )
        else:
            self.blur_level = max(
                self.blur_level - self.speed,
                0
            )

    def apply(self, frame):

        if self.blur_level < 3:
            return frame

        kernel = int(self.blur_level)

        if kernel % 2 == 0:
            kernel += 1

        return cv2.GaussianBlur(
            frame,
            (kernel, kernel),
            0
        )