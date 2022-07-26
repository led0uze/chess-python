import pygame

#white pieces
whiteBishop = pygame.transform.scale(pygame.image.load("piecesChess/foublanc.png"), (128, 128))
whitePawn = pygame.transform.scale(pygame.image.load("piecesChess/pionblanc.png"), (128, 128))
whiteRook = pygame.transform.scale(pygame.image.load("piecesChess/tourblanc.png"), (128, 128))
whiteKnight = pygame.transform.scale(pygame.image.load("piecesChess/cavalierblanc.png"), (128, 128))
whiteQueen = pygame.transform.scale(pygame.image.load("piecesChess/dameblanche.png"), (128, 128))
whiteKing = pygame.transform.scale(pygame.image.load("piecesChess/roiblanc.png"), (128, 128))

#black pieces
blackBishop = pygame.transform.scale(pygame.image.load("piecesChess/founoir.png"), (128, 128))
blackPawn = pygame.transform.scale(pygame.image.load("piecesChess/pionnoir.png"), (128, 128))
blackRook = pygame.transform.scale(pygame.image.load("piecesChess/tournoir.png"), (128, 128))
blackKnight = pygame.transform.scale(pygame.image.load("piecesChess/cavaliernoir.png"), (128, 128))
blackQueen = pygame.transform.scale(pygame.image.load("piecesChess/damenoir.png"), (128, 128))
blackKing = pygame.transform.scale(pygame.image.load("piecesChess/roinoir.png"), (128, 128))

def screenWhitePieces():
    from __main__ import screen
    piecesSize = 1024 / 8
    screen.blit(whiteRook, (1, 1))
    screen.blit(whiteKnight, (128, 1))
    screen.blit(whiteBishop, (128 * 2, 1))
    screen.blit(whiteKing, (128 * 3, 1))
    screen.blit(whiteQueen, (128 * 4, 1))
    screen.blit(whiteBishop, (128 * 5, 1))
    screen.blit(whiteKnight, (128 * 6, 1))
    screen.blit(whiteRook, (128 * 7, 1))
    screen.blit(whitePawn, (1, 128))
    for i in range(7):
        screen.blit(whitePawn, (piecesSize, 128))
        piecesSize += 128

def screenBlackPieces():
    from __main__ import screen
    piecesSize = 1024 / 8
    screen.blit(blackRook, (1, 896))
    screen.blit(blackKnight, (128, 896))
    screen.blit(blackBishop, (128 * 2, 896))
    screen.blit(blackKing, (128 * 3, 896))
    screen.blit(blackQueen, (128 * 4, 896))
    screen.blit(blackBishop, (128 * 5, 896))
    screen.blit(blackKnight, (128 * 6, 896))
    screen.blit(blackRook, (128 * 7, 896))
    screen.blit(blackPawn, (1, 768))
    for i in range(7):
        screen.blit(blackPawn, (piecesSize, 768))
        piecesSize += 128