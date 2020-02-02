import conway

import pygame
pygame.init()

BLACK = (10, 10, 10)
WHITE = (255, 255, 255)
MARGIN = 0
W = 5
H = 5

clock = pygame.time.Clock()

def renderGrid(size, elems):
    matrix = conway.initGameOfLife(size, elems)
    done = False
    while not done:

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    done = True

        for row in range(size):
            for column in range(size):
                color = BLACK
                if matrix[row][column] == 1:
                    color = WHITE
                pygame.draw.rect(screen, color, [(MARGIN + W) * column + MARGIN, (MARGIN + H) * row + MARGIN, W, H])

        matrix = conway.gameOfLife(matrix, size)

        clock.tick(60)
        pygame.display.flip()

def initDisplay(size, fullscreen):
    pygame.display.set_caption("Modus Operandi")
    if fullscreen:
        screen = pygame.display.set_mode([size[0]*5, size[1]*5] , pygame.FULLSCREEN)
    else:
        screen = pygame.display.set_mode([size[0]*5, size[1]*5])
    return screen

if __name__ == "__main__":
    size = 80
    elems = 1000

    screen = initDisplay([size, size], False)
    renderGrid(size, elems)