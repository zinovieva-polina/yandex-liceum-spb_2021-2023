# # import pygame
# #
# #
# # def draw(screen):
# #     # "Fonts/Roboto_Bold.ttf"
# #     screen.fill((0, 0, 0))
# #     font = pygame.font.Font("Fonts/Roboto-Bold.ttf", 60)
# #     text = font.render("Я сделал это!", True, (34, 255, 0))
# #     text_x = width // 2 - text.get_width() // 2
# #     text_y = height // 2 - text.get_height() // 2
# #     text_w = text.get_width()
# #     text_h = text.get_height()
# #     screen.blit(text, (text_x, text_y))
# #     pygame.draw.rect(screen, (0, 255, 0), (text_x - 10, text_y - 10,
# #                                            text_w + 20, text_h + 20), 1)
# #
# #
# # if __name__ == '__main__':
# #     # инициализация Pygame:
# #     pygame.init()
# #     # размеры окна:
# #     size = width, height = 800, 600
# #     # screen — холст, на котором нужно рисовать:
# #     screen = pygame.display.set_mode(size)
# #     # ожидание закрытия окна:
# #     while pygame.event.wait().type != pygame.QUIT:
# #         draw(screen)
# #         # смена (отрисовка) кадра:
# #         pygame.display.flip()
# #     # завершение работы:
# #     pygame.quit()
#
# import pygame
#
#
#
# razmer = int(input())
# kolvo = int(input())
# def draw(screen):
#     screen.fill((0, 0, 0))
#     pygame.draw.rect(screen, (255, 255, 255), [(0, 0), (razmer, razmer)])
#
#
#
# if __name__ == '__main__':
#     pygame.init()
#     size = width, height = 800, 600
#     screen = pygame.display.set_mode(size)
#     while pygame.event.wait().type != pygame.QUIT:
#         draw(screen)
#         pygame.display.flip()
#     pygame.quit()


import pygame

if __name__ == '__main__':
    pygame.init()
    size = width, height = 800, 400
    screen = pygame.display.set_mode(size)
    x_posr = -10
    x_posx = -10
    x_post = 200
    v = 60
    clock = pygame.time.Clock()
    running = True
    while running:
        # внутри игрового цикла ещё один цикл
        # приема и обработки сообщений
        for event in pygame.event.get():
            # при закрытии окна
            if event.type == pygame.QUIT:
                running = False
        screen.fill((255, 255, 255))
        pygame.draw.circle(screen, (247, 0, 132), (x_posr, 200), 20)
        x_posr += v * clock.tick() / 1000
        pygame.draw.circle(screen, (0, 255, 0), (x_posx, 200), 20)
        x_posx += v * clock.tick() / 1000
        # v * t в секундах
        # отрисовка и изменение свойств объектов
        # ...

        # обновление экрана
        pygame.display.flip()
    pygame.quit()

