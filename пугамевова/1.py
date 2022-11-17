import pygame

pygame.init()
FPS = 60
clock = pygame.time.Clock()
sfild = 100
otstup = 10
size = (sfild * 3 + otstup * 4, sfild * 3 + otstup * 4)

okno = pygame.display.set_mode(size)



def win(a):
    global e
    global doo
    r = 0
    if a[0][0] == r and a[0][1] == r and a[0][2] == r or a[1][0] == r and a[1][1] == r and a[1][2] == r or a[2][
        0] == r and a[2][1] == r and a[2][2] == r or a[0][0] == r and a[1][0] == r and a[2][0] == r or a[0][1] == r and \
            a[1][1] == r and a[2][1] == r or a[0][2] == r and a[1][2] == r and a[2][2] == r or a[0][0] == r and a[1][
        1] == r and a[2][2] == r or a[0][2] == r and a[1][1] == r and a[2][0] == r:
        e = 1
        print("нолики винеры")
    r = 'x'
    if a[0][0] == r and a[0][1] == r and a[0][2] == r or a[1][0] == r and a[1][1] == r and a[1][2] == r or a[2][
        0] == r and a[2][1] == r and a[2][2] == r or a[0][0] == r and a[1][0] == r and a[2][0] == r or a[0][1] == r and \
            a[1][1] == r and a[2][1] == r or a[0][2] == r and a[1][2] == r and a[2][2] == r or a[0][0] == r and a[1][
        1] == r and a[2][2] == r or a[0][2] == r and a[1][1] == r and a[2][0] == r:
        e = 1
        print("krestiki wineri")
    elif doo == 9:
        print('nu, loxi oba')


def main():
    global e
    global doo
    iq = 0
    d1 = 0
    d2 = 0
    e = 0
    doo = 0
    a = [['-'] * 3 for _ in range(3)]  # поле 50*50
    r = True
    for j in range(3):
        for i in range(3):
            color = (255, 255, 255)
            pygame.draw.rect(okno, (color), (i * sfild + otstup * (i + 1), sfild * j + otstup * (j + 1), sfild, sfild))
    while r:
        if e == 0:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    r = False
                if event.type == pygame.MOUSEBUTTONDOWN:

                    x, y = pygame.mouse.get_pos()
                    d1 = x // (sfild + otstup)
                    d2 = y // (sfild + otstup)
                    if iq == 0 and a[d2][d1] == '-':
                        a[d2][d1] = 'x'
                        iq = 1
                    elif a[d2][d1] == '-':
                        a[d2][d1] = 0
                        iq = 0
                    else:
                        print('лох, просрал ход на занятую клетку. Пошёл нахуй бот')
                    doo += 1
                    win(a)
                    okno.fill((0, 0, 0))
                    clock.tick(FPS)
                    for j in range(3):
                        for i in range(3):
                            if a[j][i] == 'x':
                                color = (0, 120, 250)
                                pygame.draw.line(okno, (color), (
                                i * sfild + otstup * (i + 1) + sfild // 10, sfild * j + otstup * (j + 1) + sfild // 10),
                                                 (i * sfild + otstup * (i + 1) + sfild - sfild // 10,
                                                  sfild * j + otstup * (j + 1) + sfild - sfild // 10), 10)
                                pygame.draw.line(okno, (color), (i * sfild + otstup * (i + 1) - sfild // 10 + sfild,
                                                                 sfild * j + otstup * (j + 1) + sfild // 10), (
                                                 i * sfild + otstup * (i + 1) + sfild + sfild // 10 - sfild,
                                                 sfild * j + otstup * (j + 1) + sfild - sfild // 10), 10)
                            elif a[j][i] == 0:
                                color = (255, 0, 0)
                                pygame.draw.circle(okno, (color), (
                                i * sfild + otstup * (i + 1) + sfild // 2, sfild * j + otstup * (j + 1) + sfild // 2),
                                                   50, 5)
                            else:
                                color = (255, 255, 255)
                                pygame.draw.rect(okno, (color), (
                                i * sfild + otstup * (i + 1), sfild * j + otstup * (j + 1), sfild,
                                sfild))  # 3-ий параметр - левый верхн угол, ширина и высота
            pygame.display.update()
        if e == 1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    r = False
    pygame.quit()


if __name__ == "__main__":
    main()
