import pygame

from Chess.pieces import *
from Chess.cvars import *



def get_mouse_pos(mp):
    x, y = mp[0], mp[1]
    row = y // SQ_SIZE
    col = x // SQ_SIZE

    return (row, col)



def main():
    run = True
    clock = pygame.time.Clock()

    while run == True:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if game.checkmate == True or game.stalemate == True:
                    pygame.quit()
                else:
                    mp = pygame.mouse.get_pos()
                    mos_pos = get_mouse_pos(mp)
                    game.click(mos_pos)
        
        game.update()

    pygame.quit()



game = Board()
main()

