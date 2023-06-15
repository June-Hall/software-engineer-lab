from map import Map
from logic import Logic
from timer import Timer
from ui import UI
import cProfile
import pstats

if __name__ == '__main__':
    map = Map(1024, 768, 10)
    logic = Logic(map)
    timer = Timer(0.02, logic)
    ui = UI(1024, 768, 10, map, logic)

    cProfile.run("ui.run()", "profile.stats")

    pstats.Stats("profile.stats").print_stats()
