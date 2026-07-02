import time


class Countdown:

    def __init__(self, duration=1.0):

        self.duration = duration

        self.start_time = None

        self.finished = False

    def start(self):

        if self.start_time is None:

            self.start_time = time.time()

            self.finished = False

    def reset(self):

        self.start_time = None

        self.finished = False

    def running(self):

        return self.start_time is not None and not self.finished

    def update(self):

        if self.start_time is None:

            return None

        elapsed = time.time() - self.start_time

        if elapsed >= self.duration:

            self.finished = True

            return 0

        ratio = elapsed / self.duration

        if ratio < 1/3:
            return 3

        elif ratio < 2/3:
            return 2

        else:
            return 1

    def scale(self):

        if self.start_time is None:

            return 1.0

        elapsed = time.time() - self.start_time

        ratio = (elapsed % (self.duration/3)) / (self.duration/3)

        return 1.0 + ratio * 0.8