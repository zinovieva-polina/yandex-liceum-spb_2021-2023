import pygame
from board.board_life import BoardGameLife


def game(screen, board):
    start = False
    FPS = 60
    tick = 0
    speed = 1
    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                board.get_click(event.pos)
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
                start = True
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                if start:
                    start = False
                else:
                    start = True
            if event.type == pygame.KEYDOWN and event.key == pygame.K_w:
                speed += 1
            if event.type == pygame.KEYDOWN and event.key == pygame.K_s:
                speed -= 1

        screen.fill((0, 0, 0))
        if start:
            if tick >= speed:
                board.next_move()
        board.render(screen)
        tick += 1
        clock.tick(FPS)
        pygame.display.flip()


if __name__ == '__main__':
    pygame.init()
    size = 470, 470
    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()
    pygame.display.set_caption('Игра «Жизнь»')

    board = BoardGameLife(30, 30, 10, 10, 15)
    game(screen, board)
