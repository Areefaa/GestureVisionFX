import time


class GestureHold:

    def __init__(self, hold_time=1.0):

        self.hold_time = hold_time

        self.start_time = None

        self.active = False

    def update(self, gesture):

        if gesture == "Victory":

            if self.start_time is None:
                self.start_time = time.time()

            elapsed = time.time() - self.start_time

            self.active = elapsed >= self.hold_time

        else:

            self.start_time = None

            self.active = False

    def progress(self):

        if self.start_time is None:
            return 0

        elapsed = time.time() - self.start_time

        return min(elapsed / self.hold_time, 1.0)