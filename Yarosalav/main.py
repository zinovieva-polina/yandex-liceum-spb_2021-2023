# import pygame
#
#
# def draw(screen):
#     # "Fonts/Roboto_Bold.ttf"
#     screen.fill((0, 0, 0))
#     font = pygame.font.Font("Fonts/Roboto-Bold.ttf", 60)
#     text = font.render("Я сделал это!", True, (34, 255, 0))
#     text_x = width // 2 - text.get_width() // 2
#     text_y = height // 2 - text.get_height() // 2
#     text_w = text.get_width()
#     text_h = text.get_height()
#     screen.blit(text, (text_x, text_y))
#     pygame.draw.rect(screen, (0, 255, 0), (text_x - 10, text_y - 10,
#                                            text_w + 20, text_h + 20), 1)
#
#
# if __name__ == '__main__':
#     # инициализация Pygame:
#     pygame.init()
#     # размеры окна:
#     size = width, height = 800, 600
#     # screen — холст, на котором нужно рисовать:
#     screen = pygame.display.set_mode(size)
#     # ожидание закрытия окна:
#     while pygame.event.wait().type != pygame.QUIT:
#         draw(screen)
#         # смена (отрисовка) кадра:
#         pygame.display.flip()
#     # завершение работы:
#     pygame.quit()

import pygame



razmer = int(input())
kolvo = int(input())
def draw(screen):
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (255, 255, 255), [(0, 0), (razmer, razmer)])



if __name__ == '__main__':
    pygame.init()
    size = width, height = 800, 600
    screen = pygame.display.set_mode(size)
    while pygame.event.wait().type != pygame.QUIT:
        draw(screen)
        pygame.display.flip()
    pygame.quit()
