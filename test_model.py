import mediapipe as mp
from mediapipe.tasks.python import vision
from mediapipe.tasks.python import BaseOptions

MODEL_PATH = "assets/models/gesture_recognizer.task"

options = vision.GestureRecognizerOptions(
    base_options=BaseOptions(model_asset_path=MODEL_PATH),
    running_mode=vision.RunningMode.IMAGE
)

recognizer = vision.GestureRecognizer.create_from_options(options)

print("✅ Model berhasil dimuat!")