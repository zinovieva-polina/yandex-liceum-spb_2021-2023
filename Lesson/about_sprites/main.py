import os
import sys
import pygame
import random


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


def game(screen):
    # создадим группу, содержащую все спрайты
    all_sprites = pygame.sprite.Group()
    # изображение должно лежать в папке data
    bomb_image = load_image("bomb.png")

    for i in range(50):
        # можно сразу создавать спрайты с указанием группы
        bomb = pygame.sprite.Sprite(all_sprites)
        bomb.image = bomb_image
        bomb.rect = bomb.image.get_rect()

        # задаём случайное местоположение бомбочке
        bomb.rect.x = random.randrange(width)
        bomb.rect.y = random.randrange(height)

    FPS = 60
    tick = 0
    image = load_image("creature.png", -1)
    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill((0, 0, 0))
        screen.blit(image, (10, 10))
        tick += 1
        clock.tick(FPS)
        pygame.display.flip()


# Изображение не получится загрузить
# без предварительной инициализации pygame
pygame.init()
size = width, height = 500, 500
screen = pygame.display.set_mode(size)
game(screen)

