class Logic:
    def __init__(self, map):
        self.map = map
        self.running = False

    def toggle_running(self):
        self.running = not self.running

    def update_map(self):
        if self.running:
            self.map.update_cells()