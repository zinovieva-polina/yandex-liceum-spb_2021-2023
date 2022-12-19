import pygame


class Character(pygame.sprite.Sprite):
    def __init__(self, sheet, columns, rows, x, y, *groups):
        super().__init__(*groups)
        self.frames = []
        self.frames_idle = []
        self.frames_walk = []
        self.cut_sheet(sheet, columns, rows)
        self.cur_frame = 0
        self.cur_frame_walk = 0
        self.image = self.frames[self.cur_frame]
        self.rect = self.rect.move(x, y)

    def cut_sheet(self, sheet, columns, rows):
        self.rect = pygame.Rect(0, 0, sheet.get_width() // columns,
                                sheet.get_height() // rows)
        for j in range(rows):
            for i in range(columns):
                frame_location = (self.rect.w * i, self.rect.h * j)
                self.frames.append(sheet.subsurface(pygame.Rect(
                    frame_location, self.rect.size)))
        # self.frames_idle = [*self.frames[:5]]
        # self.frames_walk = [*self.frames[4:15]]

    # def walk(self, event):
    #     if event.type == pygame.KEYDOWN and event.key == pygame.K_a:
    #         self.cur_frame_walk = (self.cur_frame_walk + 1) % len(self.frames_walk)
    #         self.image = self.frames_walk[self.cur_frame_walk]
    #         self.rect.x -= 10
    #     elif event.type == pygame.KEYDOWN and event.key == pygame.K_d:
    #         self.cur_frame_walk = (self.cur_frame_walk + 1) % len(self.frames_walk)
    #         self.image = self.frames_walk[self.cur_frame_walk]
    #         self.rect.x += 10
    #     else:
    #         self.cur_frame = (self.cur_frame + 1) % len(self.frames_idle)
    #         self.image = self.frames_idle[self.cur_frame]

    def update(self):
        self.cur_frame = (self.cur_frame + 1) % len(self.frames)
        self.image = self.frames[self.cur_frame]