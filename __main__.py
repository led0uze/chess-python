import pygame
from piecesChess.chessPieces import *
from chessboard import *

pygame.init()

width = 1024
cases = 8

screen = pygame.display.set_mode(size=(width, width))
pygame.display.set_caption('Echecs')
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    drawEvenLines()
    drawOddLines()
    screenWhitePieces()
    screenBlackPieces()
        

    pygame.display.update()

pygame.quit()