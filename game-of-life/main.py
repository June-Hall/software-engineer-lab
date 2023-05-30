from map import Map
from logic import Logic
from timer import Timer
from ui import UI

if __name__ == '__main__':
    map = Map(800, 600, 10)
    logic = Logic(map)
    timer = Timer(0.2, logic)
    ui = UI(800, 600, 10, map, logic)

    ui.run()
