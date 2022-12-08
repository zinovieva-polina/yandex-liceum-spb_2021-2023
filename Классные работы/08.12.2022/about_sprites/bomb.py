import pygame
import random


class Bomb(pygame.sprite.Sprite):
    def __init__(self, image, image_boom, w, h,  *group):
        # НЕОБХОДИМО вызвать конструктор родительского класса Sprite.
        # Это очень важно!!!
        super().__init__(*group)
        self.image = image
        self.image_boom = image_boom
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(w)
        self.rect.y = random.randrange(h)

    def animate_bomb(self):
        self.rect = self.rect.move(random.randrange(3) - 1,
                                   random.randrange(3) - 1)

    def explode(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(event.pos):
            self.image = self.image_boom

    def update(self, *args):
        self.animate_bomb()
        if args:
            self.explode(args[0])
