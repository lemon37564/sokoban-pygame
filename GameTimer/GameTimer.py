import time

class Timer():
    def __init__(self):
        self.elapsed = 0.0
        self.running = False
        self.last_start_time = None

    def initialize(self):
        self.elapsed = 0.0
        self.running = False
        self.last_start_time = None
        
    def start(self):
        if not self.running:
            self.running = True
            self.last_start_time = time.time()

    def pause(self):
        if self.running:
            self.running = False
            self.elapsed += time.time() - self.last_start_time

    def get_elapsed(self):
        elapsed = self.elapsed
        if self.running:
            elapsed += time.time() - self.last_start_time
        return elapsed