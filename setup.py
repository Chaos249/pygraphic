import conway as cw

import pygame
pygame.init()

BLACK = (10, 10, 10)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
MARGIN = 0
W = 5
H = 5

clock = pygame.time.Clock()

def renderGrid(size, elems, additionals):
    count = 0
    matrix = cw.initGameOfLife(size, elems)
    player_index = cw.setCharacter(matrix, size)

    done = False
    while not done:
        count += 1

        player_index = player_index
        matrix, player_index = controlPlayer(matrix, player_index)

        if additionals:
            if count % 100 == 0:
                matrix = cw.addMore(matrix, size)

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    done = True

        for row in range(size):
            for column in range(size):
                color = BLACK
                if matrix[row][column] == 1:
                    color = WHITE
                if matrix[row][column] == 2:
                    color = RED
                pygame.draw.rect(screen, color, [(MARGIN + W) * column + MARGIN, (MARGIN + H) * row + MARGIN, W, H])

        matrix = cw.gameOfLife(matrix, size)

        clock.tick(60)

        pygame.display.flip()

def initDisplay(size):
    pygame.display.set_caption("Modus Operandi")
    screen = pygame.display.set_mode([size[0]*5, size[1]*5])
    return screen

def controlPlayer(matrix, player_index):
    key = pygame.key.get_pressed()

    if key[pygame.K_LEFT]:
        matrix[player_index[1]][player_index[0]] = 0
        player_index[0] = player_index[0] - 2
        matrix[player_index[1]][player_index[0]] = 2
    if key[pygame.K_RIGHT]:
        matrix[player_index[1]][player_index[0]] = 0
        player_index[0] = player_index[0] + 2
        matrix[player_index[1]][player_index[0]] = 2
    if key[pygame.K_UP]:
        matrix[player_index[1]][player_index[0]] = 0
        player_index[1] = player_index[1] - 2
        matrix[player_index[1]][player_index[0]] = 2
    if key[pygame.K_DOWN]:
        matrix[player_index[1]][player_index[0]] = 0
        player_index[1] = player_index[1] + 2
        matrix[player_index[1]][player_index[0]] = 2

    return matrix, player_index

if __name__ == "__main__":
    size = 150
    elems = 2025

    screen = initDisplay([size, size])
    renderGrid(size, elems, True)