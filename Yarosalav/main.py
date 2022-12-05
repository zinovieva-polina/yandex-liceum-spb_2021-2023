import pygame
import pygame_menu

def create_theme_menu():
    myimage = pygame_menu.baseimage.BaseImage(
        image_path="Foto/kitchen.jpg",
        drawing_mode=pygame_menu.baseimage.IMAGE_MODE_REPEAT_XY,
        drawing_offset=(0, 0)
    )
    mytheme = pygame_menu.Theme(background_color=myimage,
                                      title_background_color=(193, 0, 113),
                                      title_font_shadow=True,
                                      widget_padding=30)
    return mytheme


def start_menu(screen, size_screen, theme_menu=None):
    menu = pygame_menu.Menu(
        height=size_screen[1],
        theme=theme_menu,
        title='Добро пожаловать',
        width=size_screen[0]
    )
    menu.add.button("Начать игру", lambda: start_game(screen))
    menu.add.button("Выход", pygame_menu.events.EXIT)
    menu.mainloop(screen)


def start_game(screen):
    running = True
    while running:
        screen.fill((255, 255, 255))
        for event in pygame.event.get():
            if event.type ** pygame.QUIT:
                running = False

        pygame.display.flip()
    pygame.quit()


if __name__ == '__main__':
    pygame.init()
    size = width, height = 900, 550
    screen = pygame.display.set_mode(size)
    start_menu(screen, size, create_theme_menu())


















































# # # import pygame
# # #
# # #
# # # def draw(screen):
# # #     # "Fonts/Roboto_Bold.ttf"
# # #     screen.fill((0, 0, 0))
# # #     font = pygame.font.Font("Fonts/Roboto-Bold.ttf", 60)
# # #     text = font.render("Я сделал это!", True, (34, 255, 0))
# # #     text_x = width // 2 - text.get_width() // 2
# # #     text_y = height // 2 - text.get_height() // 2
# # #     text_w = text.get_width()
# # #     text_h = text.get_height()
# # #     screen.blit(text, (text_x, text_y))
# # #     pygame.draw.rect(screen, (0, 255, 0), (text_x - 10, text_y - 10,
# # #                                            text_w + 20, text_h + 20), 1)
# # #
# # #
# # # if __name__ == '__main__':
# # #     # инициализация Pygame:
# # #     pygame.init()
# # #     # размеры окна:
# # #     size = width, height = 800, 600
# # #     # screen — холст, на котором нужно рисовать:
# # #     screen = pygame.display.set_mode(size)
# # #     # ожидание закрытия окна:
# # #     while pygame.event.wait().type != pygame.QUIT:
# # #         draw(screen)
# # #         # смена (отрисовка) кадра:
# # #         pygame.display.flip()
# # #     # завершение работы:
# # #     pygame.quit()
# #
# # import pygame
# #
# #
# #
# # razmer = int(input())
# # kolvo = int(input())
# # def draw(screen):
# #     screen.fill((0, 0, 0))
# #     pygame.draw.rect(screen, (255, 255, 255), [(0, 0), (razmer, razmer)])
# #
# #
# #
# # if __name__ == '__main__':
# #     pygame.init()
# #     size = width, height = 800, 600
# #     screen = pygame.display.set_mode(size)
# #     while pygame.event.wait().type != pygame.QUIT:
# #         draw(screen)
# #         pygame.display.flip()
# #     pygame.quit()
#
#
# #         screen.fill((230, 215, 7))
# #         pygame.draw.circle(screen, (247, 0, 132), (x_posr, 200), 20)
# #         x_posr += v / fps + 1
# #         pygame.draw.circle(screen, (0, 255, 0), (x_posx, 175), 5)
# #         x_posx += v / fps + 1
# #         pygame.draw.circle(screen, (0, 0, 0), (x_posl, 194), 5)
# #         x_posl += v / fps + 1
# #         pygame.draw.circle(screen, (0, 0, 0), (x_posre, 194), 5)
# #         x_posre += v / fps + 1
# #         pygame.draw.circle(screen, (255, 255, 255), (x_posrot, 210), 5)
# #         x_posrot += v / fps + 1
# #         pygame.draw.rect(screen, (107, 106, 95), ((x_pram, 90), (80, 130)))
# #         x_pram += v / fps
# #         pygame.draw.circle(screen, (0, 0, 0), (x_pramr, 120), 10)
# #         x_pramr += v / fps
# #         pygame.draw.circle(screen, (0, 0, 0), (x_praml, 120), 10)
# #         x_praml += v / fps
#
# # # 2 версия проекта
# #
# import pygame
#
# if __name__ == '__main__':
#     pygame.init()
#     size = width, height = 800, 400
#     screen = pygame.display.set_mode(size)
#     background_image = pygame.image.load("Foto/kitchen.jpg")
#
#     running = True
#     '''РЕДИСКА'''
#     x_pos = 30  # тело
#     y_pos = 280  # тело
#     x_posl = 41  # правый глаз
#     y_posl = 280  # правый глаз
#     x_posrz = 41  # правый глаз зрачок
#     y_posrz = 280  # правый глаз зрачок
#
#     x_poslz = 21  # левый глаз зрачок
#     y_poslz = 280  # левый глаз зрачок
#     x_posr = 21  # левый глаз
#     y_posr = 280  # левый глаз
#     x_hvost = 30
#     y_hvost = 247
#
#     '''ТЁРКА'''
#     # x_pos1 = -60  # тёрка
#     # y_pos2 = 180  # тёрка
#     # x_posrt = 21  # левый глаз
#     x_prami = -90
#     x_pramr = -60
#     x_praml = -57
#     x_pramrr = -20
#     x_pramll = -17
#
#
#
#
#     v = 480  # пикселей в секунду
#     fps2 = 45  # скорость тёрки
#     fps = 30
#     clock = pygame.time.Clock()
#     while running:
#         screen.blit(background_image, (0, 0))
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 running = False
#
#             if event.type == pygame.KEYUP:
#                 if event.key == pygame.K_LEFT:
#                     x_pos -= v / fps
#                     x_posl -= v / fps
#                     x_posr -= v / fps
#                     x_posrz -= v / fps
#                     x_poslz -= v / fps
#                     x_hvost -= v / fps
#
#                 if event.key == pygame.K_RIGHT:
#                     x_pos += v / fps
#                     x_posl += v / fps
#                     x_posr += v / fps
#                     x_posrz += v / fps
#                     x_poslz += v / fps
#                     x_hvost += v / fps
#
#             # if event.type == pygame.KEYDOWN:
#             #     if event.key == pygame.K_UP:
#             #         y_pos -= v / fps
#             #         y_posl -= v / fps
#             #         y_posr -= v / fps
#             #         y_posrz -= v / fps
#             #         y_poslz -= v / fps
#             #         y_hvost -= v / fps
#             #
#             #     if event.key == pygame.K_DOWN:
#             #         y_pos += v / fps
#             #         y_posl += v / fps
#             #         y_posr += v / fps
#             #         y_posrz += v / fps
#             #         y_poslz += v / fps
#             #         y_hvost -= v / fps
#
#         pygame.draw.circle(screen, (235, 28, 133), (int(x_pos), int(y_pos)), 30)  # тело
#         pygame.draw.circle(screen, (255, 255, 255), (int(x_posl), int(y_posl)), 8)  # левый глаз
#         pygame.draw.circle(screen, (255, 255, 255), (int(x_posr), int(y_posr)), 8)  # правый глаз
#         pygame.draw.circle(screen, (0, 0, 0), (int(x_posrz), int(y_posrz)), 5)  # правый глаз зрачок
#         pygame.draw.circle(screen, (0, 0, 0), (int(x_poslz), int(y_poslz)), 5) # левый глаз зрачок
#         pygame.draw.circle(screen, (0, 255, 31), (int(x_hvost), int(y_hvost)), 5) #хвостик
#         pygame.draw.rect(screen, (107, 106, 95), ((x_prami, 180), (80, 130))) # терка
#         x_prami += v / fps2 - 10
#         pygame.draw.circle(screen, (159, 0, 30), (x_pramr, 210), 10)
#         x_pramr += v / fps2 - 10
#         pygame.draw.circle(screen, (0, 0, 0), (x_praml, 210), 5)
#         x_praml += v / fps2 - 10
#         pygame.draw.circle(screen, (255, 0, 0), (x_pramrr, 210), 10)
#         x_pramrr += v / fps2 - 10
#         pygame.draw.circle(screen, (0, 0, 0), (x_pramll, 210), 5)
#         x_pramll += v / fps2 - 10
#         # pygame.draw.rect(screen, (160, 163, 166), (int(x_pos1), int(y_pos2), 70, 150))  # тёрка
#         # pygame.draw.circle(screen, (0, 0, 0), (int(x_posrr), int(x_posrl)), 5)  # правый глаз зрачок
#         # pygame.draw.circle(screen, (0, 0, 0), (int(x_posrt), int(x_posrt)), 5)  # левый глаз зрачок
#         # pygame.draw.circle(screen, (255, 255, 255), (int(x_posl), int(y_posl)), 8)  # левый глаз
#         # pygame.draw.circle(screen, (255, 255, 255), (int(x_posr), int(y_posr)), 8)  # правый глаз
#         # x_pos1 += vt * clock.tick() / 1000 # v * t в секундах
#         # y_pos2 += vt * clock.tick() / 1000
#
#         clock.tick(fps)
#         pygame.display.flip()
#     pygame.quit()