import time

class Timer:
    def __init__(self, interval, logic):
        self.interval = interval
        self.logic = logic
        self.last_update_time = time.time()

    def update(self):
        current_time = time.time()
        if current_time - self.last_update_time >= self.interval:
            self.logic.update_map()
            self.last_update_time = current_time