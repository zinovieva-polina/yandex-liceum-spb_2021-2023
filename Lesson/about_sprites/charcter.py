import pygame


class Character(pygame.sprite.Sprite):
    def __init__(self, image, coord, speed,  *group):
        # НЕОБХОДИМО вызвать конструктор родительского класса Sprite.
        # Это очень важно!!!
        super().__init__(*group)
        self.image = image
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = coord[0]
        self.rect.y = coord[1]

    def walk(self, event):
        if event.type == pygame.KEYDOWN and event.key == pygame.K_w:
            self.rect.y -= self.speed
        if event.type == pygame.KEYDOWN and event.key == pygame.K_a:
            self.rect.x -= self.speed
        if event.type == pygame.KEYDOWN and event.key == pygame.K_s:
            self.rect.y += self.speed
        if event.type == pygame.KEYDOWN and event.key == pygame.K_d:
            self.rect.x += self.speed

    def update(self, *args):
        if args:
            self.walk(args[0])
