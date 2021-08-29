import pygame

WIDTH, HEIGHT = 800, 800
ROWS, COLS = 8, 8
SQ_SIZE = WIDTH // COLS

PURPLE = (151, 111 , 212)
BEIGE = (214, 223, 175)
GREEN = (20, 205, 14)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

FPS = 60

WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Chess")

bPAWN = pygame.image.load("ChessAssets/bPawn.png")
wPAWN = pygame.image.load("ChessAssets/wPawn.png")

bKNIGHT = pygame.image.load("ChessAssets/bKnight.png")
wKNIGHT = pygame.image.load("ChessAssets/wKnight.png")

bBISHOP = pygame.image.load("ChessAssets/bBishop.png")
wBISHOP = pygame.image.load("ChessAssets/wBishop.png")

bROOK = pygame.image.load("ChessAssets/bRook.png")
wROOK = pygame.image.load("ChessAssets/wRook.png")

bQUEEN = pygame.image.load("ChessAssets/bQueen.png")
wQUEEN = pygame.image.load("ChessAssets/wQueen.png")

bKING = pygame.image.load("ChessAssets/bKing.png")
wKING = pygame.image.load("ChessAssets/wKing.png")

pro_QUEEN = pygame.image.load("ChessAssets/pQueen.png")
pro_ROOK = pygame.image.load("ChessAssets/pRook.png")
pro_KNIGHT = pygame.image.load("ChessAssets/pKnight.png")
pro_BISHOP = pygame.image.load("ChessAssets/pBishop.png")

piece_SELECT = pygame.image.load("ChessAssets/piece_select.png")

castle_icon = pygame.image.load("ChessAssets/castle_icon.png")

start_CHESS = pygame.image.load("ChessAssets/start_chess.png")
start_FLASH = pygame.image.load("ChessAssets/starting.png")

red_MATE = pygame.image.load("ChessAssets/redmate.png")
blue_MATE = pygame.image.load("ChessAssets/bluemate.png")

stale_MATE = pygame.image.load("ChessAssets/stalemate.png")