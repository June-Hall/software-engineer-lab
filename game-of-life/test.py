import unittest
import time
import pygame
from map import Map
from logic import Logic
from timer import Timer
from ui import UI


class MapTestCase(unittest.TestCase):
    def setUp(self):
        self.map = Map(10, 10, 1)
        
    def test_set_cell_state(self):
        self.map.set_cell_state(3, 5, 1)
        self.assertEqual(self.map.get_cell_state(3, 5), 1)
        
    def test_get_cell_state(self):
        self.map.cells[3, 5] = 1
        self.assertEqual(self.map.get_cell_state(3, 5), 1)
        
    def test_update_cells(self):
        expected_cells = self.map.cells
        expected_cells[2, 3] = 1
        self.map.cells[3, 1] = 1
        self.map.cells[3, 3] = 1
        self.map.cells[2, 2] = 1

        self.map.update_cells()

        self.assertEqual(self.map.cells[2, 3], expected_cells[2, 3])

class LogicTestCase(unittest.TestCase):
    def setUp(self):
        map = Map(10, 10, 1)
        self.logic = Logic(map)
        
    def test_toggle_running(self):
        self.logic.toggle_running()
        self.assertTrue(self.logic.running)
        self.logic.toggle_running()
        self.assertFalse(self.logic.running)
        
    def test_update_map(self):
        self.logic.running = True

        expected_cells = self.logic.map.cells
        expected_cells[2, 3] = 1
        self.logic.map.cells[3, 1] = 1
        self.logic.map.cells[3, 3] = 1
        self.logic.map.cells[2, 2] = 1

        self.logic.update_map()

        self.assertEqual(self.logic.map.cells[2, 3], expected_cells[2, 3])

class TimerTestCase(unittest.TestCase):
    def setUp(self):
        map = Map(10, 10, 1)
        logic = Logic(map)
        self.timer = Timer(0.1, logic)
        
    def test_update(self):
        expected_cells = self.timer.logic.map.cells
        expected_cells[2, 3] = 1
        self.timer.logic.map.cells[3, 1] = 1
        self.timer.logic.map.cells[3, 3] = 1
        self.timer.logic.map.cells[2, 2] = 1
        time.sleep(0.2)
        self.timer.update()
        self.assertEqual(self.timer.logic.map.cells[2, 3], expected_cells[2, 3])

class UITestCase(unittest.TestCase):
    def setUp(self):
        map = Map(800, 600, 10)
        logic = Logic(map) 
        self.ui = UI(800, 600, 10, map, logic)
        
    def test_init_screen(self):
        self.ui.init_screen()
        screen = pygame.display.get_surface()
        self.assertNotEqual(screen, None)
        
    def test_update_cells(self):
        self.ui.map.cells[3, 3] = 1
        self.ui.update_cells()
        screen = pygame.display.get_surface()
        pixel_color = screen.get_at((30, 30))
        self.assertEqual(pixel_color, (255, 255, 255))
        
    def test_run(self):
        pygame.init()
        event = self.ui.run()
        self.assertTrue(event)

if __name__ == '__main__':    
    unittest.main()