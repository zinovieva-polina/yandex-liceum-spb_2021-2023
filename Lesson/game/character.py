import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self, image, pos,  speed, *group):
        super().__init__(*group)
        self.image = image
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]

    def walk(self, event):
        if event.type == pygame.KEYDOWN and event.key == pygame.K_a:
            self.rect.x -= self.speed
        if event.type == pygame.KEYDOWN and event.key == pygame.K_d:
            self.rect.x += self.speed

    # def fall(self):
    #     if pygame.sprite.spritecollideany(self, self.platform_group) is None:
    #         self.rect.y += self.speed

    def update(self, *args):
        if args:
            self.walk(args[0])
