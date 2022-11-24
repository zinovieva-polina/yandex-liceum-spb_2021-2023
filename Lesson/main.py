import pygame

if __name__ == '__main__':
    pygame.init()
    size = width, height = 800, 400
    screen = pygame.display.set_mode(size)
    x_pos = 0
    v = 60  # пикселей в секунду
    fps = 50  # количество кадров в секунду
    clock = pygame.time.Clock()
    running = True
    while running:  # главный игровой цикл
        screen.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                      x_pos += v / fps  # v * t в секундах

        pygame.draw.circle(screen, (255, 0, 0), (int(x_pos), 200), 20)

        # обработка остальных событий
        # ...
        # формирование кадра
        # ...

        pygame.display.flip()  # смена кадра
        # изменение игрового мира
        # ...
        # временная задержка
        clock.tick(fps)
    pygame.quit()