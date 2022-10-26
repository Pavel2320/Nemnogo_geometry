import pygame

pygame.init()

WIDTH, HEIGHT = 800, 600
FPS = 60
window = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

x1, y1 = WIDTH // 8, HEIGHT
x2, y2 = 0, 0
x3, y3 = WIDTH, 0
t = 0

play = True
while play:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False

    x4, y4 = pygame.mouse.get_pos()
    #   Время полета: кол-во итераций / FPS
    t += 1 / 400
    if t > 1.5:
        t = 0
    #   Кривая Безье 4-го порядка
    x = (1 - t) ** 3 * x1 + 3 * (1 - t) ** 2 * t * x2 + 3 * (1 - t) * t ** 2 * x3 + t ** 3 * x4
    y = (1 - t) ** 3 * y1 + 3 * (1 - t) ** 2 * t * y2 + 3 * (1 - t) * t ** 2 * y3 + t ** 3 * y4

    window.fill('black')
    for d in range(151):
        dd = d / 100
        dx = (1 - dd) ** 3 * x1 + 3 * (1 - dd) ** 2 * dd * x2 + 3 * (1 - dd) * dd ** 2 * x3 + dd ** 3 * x4
        dy = (1 - dd) ** 3 * y1 + 3 * (1 - dd) ** 2 * dd * y2 + 3 * (1 - dd) * dd ** 2 * y3 + dd ** 3 * y4
        pygame.draw.circle(window, 'khaki', (dx, dy), 2)

    pygame.draw.circle(window, 'blue', (x1, y1), 10)
    pygame.draw.circle(window, 'gray', (x2, y2), 15)
    pygame.draw.circle(window, 'ivory', (x3, y3), 15)
    pygame.draw.circle(window, 'red', (x4, y4), 10)
    pygame.draw.circle(window, 'yellow', (x, y), 10)

    pygame.display.update()
    clock.tick(FPS)
pygame.quit()
