import pygame


def draw(screen, w, h):
    screen.fill((0, 0, 0))
    pygame.draw.line(screen, (255, 255, 255),
                     [0, 0],
                     [w, h], 5)
    pygame.draw.line(screen, (255, 255, 255),
                     [w, 0],
                     [0, h], 5)


if __name__ == '__main__':
    pygame.init()
    sz = input().split()
    width, height = int(sz[0]), int(sz[1])
    size = width, height
    screen = pygame.display.set_mode(size)


while pygame.event.wait().type != pygame.QUIT:
    draw(screen, width, height)
    pygame.display.flip()
pygame.quit()