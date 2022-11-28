import pygame
from board import Board


def game(screen, board):
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill((0, 0, 0))
        board.render(screen)
        pygame.display.flip()


if __name__ == '__main__':
    pygame.init()
    size = width, height = 800, 400
    screen = pygame.display.set_mode(size)
    # поле 5 на 7
    board = Board(4, 3)
    board.set_view(100, 100, 50)
    game(screen, board)
