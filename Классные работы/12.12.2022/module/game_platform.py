import pygame


class Platform(pygame.sprite.Sprite):
    def __init__(self, image, pos, *group):
        super().__init__(*group)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]