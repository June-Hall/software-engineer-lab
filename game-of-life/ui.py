import time
import pygame
import numpy as np
from map import Map
from logic import Logic
from timer import Timer

COLOR_BG = (10, 10, 10)             # 背景颜色
COLOR_GRID = (40, 40, 40)           # 网格颜色
COLOR_DIE_NEXT = (170, 170, 170)    # 下一代死细胞颜色
COLOR_ALIVE_NEXT = (255, 255, 255)  # 下一代存活细胞颜色

class UI:
    def __init__(self, width, height, cell_size, map, logic):
        self.width = width
        self.height = height
        self.cell_size = cell_size
        self.map = map
        self.logic = logic

        pygame.init()
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Game of Life")

    def init_screen(self):
        self.screen.fill(COLOR_GRID)
        self.update_cells()
        pygame.display.update()

    def update_cells(self):
        for row, col in np.ndindex(self.map.cells.shape):
            color = COLOR_BG if self.map.get_cell_state(row, col) == 0 else COLOR_ALIVE_NEXT
            pygame.draw.rect(
                self.screen, color,
                (col * self.cell_size, row * self.cell_size, self.cell_size - 1, self.cell_size - 1)
            )

    def run(self):
        self.init_screen()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return event
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.logic.toggle_running()
                        pygame.display.update()
                if pygame.mouse.get_pressed()[0]:
                    pos = pygame.mouse.get_pos()
                    row = pos[1] // self.cell_size
                    col = pos[0] // self.cell_size
                    self.map.set_cell_state(row, col, 1)
                    self.update_cells()
                    pygame.display.update()

            
            if self.logic.running:
                self.map.update_cells()
            self.screen.fill(COLOR_GRID)
            self.update_cells()

            pygame.display.update()
            time.sleep(0.001)