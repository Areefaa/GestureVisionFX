import cv2
import time


class UI:

    def __init__(self):

        self.message = ""

        self.show_until = 0

        self.fade_time = 0.5

        self.display_time = 2

    def show(self, text):

        self.message = text

        self.show_until = time.time() + self.display_time

    def draw(self, frame, gesture):

        if self.message == "":
            return frame

        now = time.time()

        remain = self.show_until - now

        if remain <= 0:

            self.message = ""

            return frame

        total = self.display_time

        elapsed = total - remain

        if elapsed < self.fade_time:

            alpha = elapsed / self.fade_time

        elif remain < self.fade_time:

            alpha = remain / self.fade_time

        else:

            alpha = 1

        overlay = frame.copy()

        text = self.message

        font = cv2.FONT_HERSHEY_DUPLEX

        scale = 1.1

        thickness = 2

        (w,h), _ = cv2.getTextSize(
            text,
            font,
            scale,
            thickness
        )

        x = (frame.shape[1]-w)//2

        y = frame.shape[0]-70

        cv2.putText(
            overlay,
            text,
            (x,y),
            font,
            scale,
            (255,255,255),
            thickness
        )

        return cv2.addWeighted(
            overlay,
            alpha,
            frame,
            1-alpha,
            0
        )