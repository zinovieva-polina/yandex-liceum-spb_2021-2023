import pygame
from module.character import Character
from module.game_platform import Platform
import sys
import os


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


def game(screen, background_game_img):
    # создадим группу, содержащую все спрайты
    FPS = 60
    tick = 0
    clock = pygame.time.Clock()
    hero = None
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if hero is None:
                        hero = Character(load_image("character_idle.png"), event.pos, 10, platform_group, player_group, all_sprites)
                    else:
                        hero.rect.x = event.pos[0]
                        hero.rect.y = event.pos[1]
                if event.button == 3:
                    Platform(load_image("platform.png"), event.pos, platform_group, all_sprites)
            player_group.update(event)
        screen.fill((0, 0, 0))
        screen.blit(background_game_img, (0, 0))
        all_sprites.draw(screen)
        if hero:
            hero.fall()
        tick += 1
        clock.tick(FPS)
        pygame.display.flip()


if __name__ == '__main__':
    pygame.init()
    background_game_img = pygame.image.load("data/background.png")
    size = width, height = 500, 500
    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()
    pygame.display.set_caption('Мини-платформер')
    all_sprites = pygame.sprite.Group()
    platform_group = pygame.sprite.Group()
    player_group = pygame.sprite.Group()
    game(screen, background_game_img)
