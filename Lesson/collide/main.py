import pygame
from character import Character
from game_platform import Platform


def game(screen, background_game_img):
    # создадим группу, содержащую все спрайты
    FPS = 60
    tick = 0
    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill((0, 0, 0))
        screen.blit(background_game_img, (0, 0))
        tick += 1
        clock.tick(FPS)
        pygame.display.flip()


if __name__ == '__main__':
    pygame.init()
    size = width, height = 500, 500
    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()
    pygame.display.set_caption('Мини-платформер')
    background_game_img = pygame.image.load("data/background.png")

    game(screen, background_game_img)
