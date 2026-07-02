import mediapipe as mp

mp_hands = mp.solutions.hands


class HandGestureDetector:
    def __init__(self):
        self.hands = mp_hands.Hands(
            static_image_mode=False,
            max_num_hands=1,
            min_detection_confidence=0.7,
            min_tracking_confidence=0.7,
        )

    def is_peace(self, frame):
        rgb = frame[:, :, ::-1]
        results = self.hands.process(rgb)

        if not results.multi_hand_landmarks:
            return False

        hand = results.multi_hand_landmarks[0]

        lm = hand.landmark

        # Tip dan PIP
        index_tip = lm[8]
        index_pip = lm[6]

        middle_tip = lm[12]
        middle_pip = lm[10]

        ring_tip = lm[16]
        ring_pip = lm[14]

        pinky_tip = lm[20]
        pinky_pip = lm[18]

        # Jari terbuka jika tip lebih tinggi
        index_open = index_tip.y < index_pip.y
        middle_open = middle_tip.y < middle_pip.y

        ring_closed = ring_tip.y > ring_pip.y
        pinky_closed = pinky_tip.y > pinky_pip.y

        if index_open and middle_open and ring_closed and pinky_closed:
            return True

        return False