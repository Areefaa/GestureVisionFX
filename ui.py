import cv2


class UI:

    def __init__(self):

        self.alpha = 0.0
        self.speed = 0.04

    def draw(self, frame, gesture):

        if gesture == "Victory":
            self.alpha = min(self.alpha + self.speed, 1.0)
        else:
            self.alpha = max(self.alpha - self.speed, 0.0)

        # Gesture text
        color = (0,255,0) if gesture else (0,0,255)

        cv2.putText(
            frame,
            f"Gesture : {gesture}",
            (20,40),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            color,
            2
        )

        # ==========================
        # Foto Kita Blur...
        # ==========================

        if self.alpha > 0:

            overlay = frame.copy()

            text = "Foto Kita Blur..."

            font = cv2.FONT_HERSHEY_DUPLEX

            scale = 1.2

            thickness = 2

            size = cv2.getTextSize(
                text,
                font,
                scale,
                thickness
            )[0]

            x = (frame.shape[1]-size[0])//2
            y = frame.shape[0]-60

            cv2.putText(
                overlay,
                text,
                (x,y),
                font,
                scale,
                (255,255,255),
                thickness
            )

            frame = cv2.addWeighted(
                overlay,
                self.alpha,
                frame,
                1-self.alpha,
                0
            )

        return frame