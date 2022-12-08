import pygame
from sasha.gamelife.board.board import Board
import copy


class BoardGameLife(Board):
    # создание поля
    def __init__(self, width, height, left=10, top=10, cell_size=30):
        super().__init__(width, height, left, top, cell_size)

    def change_state_cell(self, cell):
        self.board[cell[0]][cell[1]] = (self.board[cell[0]][cell[1]] + 1) % 2

    def on_click(self, cell):
        # cell - кортеж (x, y)
        # заглушка для реальных игровых полей
        self.change_state_cell(cell)
        print(cell, self.board[cell[0]][cell[1]])

    def render(self, screen):
        coord_x, coord_y = self.left, self.top
        for row in range(len(self.board)):
            for col in range(len(self.board[0])):
                if self.board[col][row]:
                    pygame.draw.rect(screen, (0, 255, 0), ((coord_x, coord_y), (self.cell_size, self.cell_size)))
                    coord_x += self.cell_size
                else:
                    pygame.draw.rect(screen, (255, 255, 255), ((coord_x, coord_y), (self.cell_size, self.cell_size)), 1)
                    coord_x += self.cell_size
            coord_y += self.cell_size
            coord_x = self.left

    def next_move(self):
        board = copy.deepcopy(self.board)
        for row in range(len(board)):
            for col in range(len(board[0])):
                sum_neighbours = 0
                for dx in range(-1, 2):
                    for dy in range(-1, 2):
                        if (row + dx >= 0 and row + dx < len(board)) and (col + dy >= 0 and col + dy < len(board)):
                            sum_neighbours += board[row + dx][col + dy]
                sum_neighbours -= board[row][col]
                if sum_neighbours == 3:
                    board[row][col] = 1
                elif sum_neighbours < 2 or sum_neighbours > 3:
                    board[row][col] = 0
        self.board = copy.deepcopy(board)




