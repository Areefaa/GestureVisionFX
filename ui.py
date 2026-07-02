import cv2


class UI:

    def draw(self, frame, gesture):

        if gesture:

            text = f"Gesture : {gesture}"
            color = (0,255,0)

        else:

            text = "Gesture : None"
            color = (0,0,255)

        cv2.putText(
            frame,
            text,
            (20,40),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            color,
            2
        )

        return frame