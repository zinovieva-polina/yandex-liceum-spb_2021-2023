import pygame


class Board:
    # создание поля
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]
        # значения по умолчанию
        self.left = 10
        self.top = 10
        self.cell_size = 30

    # настройка внешнего вида
    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def render(self, screen):
        coord_x, coord_y = self.left, self.top
        for row in range(len(self.board)):
            for col in range(len(self.board[0])):
                pygame.draw.rect(screen, (255, 255, 255), ((coord_x, coord_y), (self.cell_size, self.cell_size)), 1)
                coord_x += self.cell_size
            coord_y += self.cell_size
            coord_x = self.left



