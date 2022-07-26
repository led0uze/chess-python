import pygame

def drawOddLines():
    from __main__ import screen, width, cases
    x1 = 0
    y1 = width / cases
    x2 = width / cases
    y2 = width / cases
    for i in range(4):
        for i in range(4):
            pygame.draw.rect(screen, (60, 43, 21), (x1, y1, x2, y2))
            x1 += width / cases
            pygame.draw.rect(screen, (194, 167, 124), (x1, y1, x2, y2))
            x1 += width / cases
        y1 += width / cases * 2
        x1 = 0

def drawEvenLines():
    from __main__ import screen, width, cases
    x1 = 0
    y1 = 0
    x2 = width / cases
    y2 = width / cases
    for i in range(4):
        for i in range(4):
            pygame.draw.rect(screen, (194, 167, 124), (x1, y1, x2, y2))
            x1 += width / cases
            pygame.draw.rect(screen, (60, 43, 21), (x1, y1, x2, y2))
            x1 += width / cases
        y1 += width / cases * 2
        x1 = 0