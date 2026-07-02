import time
import cv2
import mediapipe as mp

from mediapipe.tasks.python import vision
from mediapipe.tasks.python import BaseOptions


class GestureDetector:

    def __init__(self, model_path):

        options = vision.GestureRecognizerOptions(
            base_options=BaseOptions(model_asset_path=model_path),
            running_mode=vision.RunningMode.LIVE_STREAM,
            num_hands=1,
            result_callback=self._callback
        )

        self.recognizer = vision.GestureRecognizer.create_from_options(options)

        self.current_gesture = None

    def _callback(self, result, output_image, timestamp_ms):

        if len(result.gestures) == 0:
            self.current_gesture = None
            return

        self.current_gesture = result.gestures[0][0].category_name

    def detect(self, frame):

        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        image = mp.Image(
            image_format=mp.ImageFormat.SRGB,
            data=rgb
        )

        timestamp = int(time.time() * 1000)

        self.recognizer.recognize_async(
            image,
            timestamp
        )

        return self.current_gesture