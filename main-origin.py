import time
import pygame
import numpy as np

COLOR_BG = (10, 10, 10)             # 背景颜色
COLOR_GRID = (40, 40, 40)           # 网格颜色
COLOR_DIE_NEXT = (170, 170, 170)    # 下一代死细胞颜色
COLOR_ALIVE_NEXT = (255, 255, 255)  # 下一代存活细胞颜色

# 原来的代码
class GameOfLife:
    def __init__(self, width, height, cell_size):
        self.width = width               # 宽度
        self.height = height             # 高度
        self.cell_size = cell_size       # 细胞尺寸
        self.screen = pygame.display.set_mode(
            (self.width, self.height))  # 创建游戏窗口
        self.cells = np.zeros(
            (self.height // self.cell_size, self.width // self.cell_size))  # 存储细胞状态的二维数组
        self.running = False             # 运行标志

        pygame.init()  # 初始化 Pygame
        pygame.display.set_caption("Game of Life")

    def init_screen(self):
        self.screen.fill(COLOR_GRID)  # 填充窗口背景颜色
        self.update_cells()  # 更新细胞状态
        pygame.display.update()

    def clean_screen(self):
        self.screen.fill(COLOR_GRID)

    def run(self):
        self.init_screen()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:  # 退出游戏
                    pygame.quit()
                    return
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:  # 空格键切换游戏运行状态
                        self.running = not self.running
                        self.update_cells()
                        pygame.display.update()
                if pygame.mouse.get_pressed()[0]:  # 按下鼠标，将对应位置的细胞状态设为存活
                    pos = pygame.mouse.get_pos()
                    self.cells[pos[1] // self.cell_size, pos[0] //
                               self.cell_size] = 1
                    self.update_cells()
                    pygame.display.update()

            self.clean_screen()  # 清空屏幕，准备绘制下一帧

            if self.running:
                self.cells = self.update_cells(
                    with_progress=True)  # 更新细胞状态并获取下一代细胞状态
                pygame.display.update()  # 更新部分窗口的显示

            time.sleep(0.001)  # 控制游戏循环的速度

    def update_cells(self, with_progress=False):
        # 创建一个与当前细胞状态相同的数组用于存储下一代细胞状态
        updated_cells = np.zeros_like(self.cells)

        for row, col in np.ndindex(self.cells.shape):
            # 统计周围存活细胞的数量
            alive = np.sum(self.cells[row - 1: row + 2, col -
                           1: col + 2]) - self.cells[row, col]
            # 根据细胞状态确定绘制的颜色
            color = COLOR_BG if self.cells[row, col] == 0 else COLOR_ALIVE_NEXT

            if self.cells[row, col] == 1:  # 当前细胞存活
                if alive < 2 or alive > 3:
                    if with_progress:
                        color = COLOR_DIE_NEXT
                elif 2 <= alive <= 3:
                    updated_cells[row, col] = 1
                    if with_progress:
                        color = COLOR_ALIVE_NEXT
            else:  # 当前细胞死亡
                if alive == 3:
                    updated_cells[row, col] = 1
                    if with_progress:
                        color = COLOR_ALIVE_NEXT

            pygame.draw.rect(
                self.screen, color, (col * self.cell_size, row *
                                     self.cell_size, self.cell_size - 1, self.cell_size - 1)
            )

        return updated_cells


if __name__ == '__main__':
    game = GameOfLife(800, 600, 10)
    game.run()
