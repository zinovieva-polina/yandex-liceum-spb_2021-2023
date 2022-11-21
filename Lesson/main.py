import pygame


def draw(screen):
    screen.fill((0, 0, 0))
    font = pygame.font.Font("fonts/RubikDistressed-Regular.ttf", 20)
    text = font.render("Hello, Pygame!", True, (100, 255, 100))
    text_x = width // 2 - text.get_width() // 2
    text_y = height // 2 - text.get_height() // 2
    text_w = text.get_width()
    text_h = text.get_height()
    screen.blit(text, (text_x, text_y))
    pygame.draw.rect(screen, (0, 255, 0), (text_x - 10, text_y - 10,
                                           text_w + 20, text_h + 20), 1)


if __name__ == '__main__':
    # инициализация Pygame:
    pygame.init()
    # размеры окна:
    size = width, height = 800, 600
    # screen — холст, на котором нужно рисовать:
    screen = pygame.display.set_mode(size)
    flag = True
    x = 0
    # ожидание закрытия окна:
    while pygame.event.wait().type != pygame.QUIT:
        if flag:
            x += 10
        else:
            x -= 10
        if x >= width:
            flag = False
        elif x <= 0:
            flag = True
        draw(screen)
        pygame.draw.rect(screen, (0, 255, 0), (x, 0, 40, 40), 1)

        # смена (отрисовка) кадра:
        pygame.display.flip()
    # завершение работы:
    pygame.quit()