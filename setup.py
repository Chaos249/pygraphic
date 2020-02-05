import conway as cw

import pygame
pygame.init()

BLACK = (10, 10, 10)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
MARGIN = 0
W = 5
H = 5

clock = pygame.time.Clock()

def renderGrid(size, elems, additionals, screen):
    count = 0
    board_points = 0
    player_points = 0
    matrix = cw.initGameOfLife(size, elems)
    player_index = cw.setCharacter(matrix, size)

    done = False
    state = False
    while not done:
        count += 1

        player_index = player_index
        matrix, player_index = controlPlayer(matrix, player_index)

        if additionals:
            if count % 100 == 0:
                matrix = cw.addMore(matrix, size)
            if count % 25 == 0 and board_points <= 10:
                matrix = cw.addBoardPoints(matrix, size)
                board_points += 1
            if count < 20:
                text_to_screen(screen, "Modus Operandi", (size//2), (size//2))

        if state:
            done = True

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
                if matrix[row][column] == 3:
                    color = GREEN
                pygame.draw.rect(screen, color, [(MARGIN + W) * column + MARGIN, (MARGIN + H) * row + MARGIN, W, H])

        matrix, state, added_points = cw.gameOfLife(matrix, size)
        player_points += added_points

        clock.tick(60)

        pygame.display.flip()

def initDisplay(size):
    pygame.display.set_caption("Modus Operandi")
    screen = pygame.display.set_mode([size[0]*5, size[1]*5])
    return screen

def text_to_screen(screen, text, x, y, size = 50,
    color = (WHITE), font_type = 'freesansbold.ttf'):
    try:
        text = str(text)
        font = pygame.font.Font(font_type, size)
        text = font.render(text, True, color)
        screen.blit(text, (x, y))
    except:
        print ('Font Error, saw it coming')

def controlPlayer(matrix, player_index):
    key = pygame.key.get_pressed()

    if key[pygame.K_LEFT]:
        matrix[player_index[1]][player_index[0]] = 0
        player_index[0] = player_index[0] - 1
        matrix[player_index[1]][player_index[0]] = 2
    if key[pygame.K_RIGHT]:
        matrix[player_index[1]][player_index[0]] = 0
        player_index[0] = player_index[0] + 1
        matrix[player_index[1]][player_index[0]] = 2
    if key[pygame.K_UP]:
        matrix[player_index[1]][player_index[0]] = 0
        player_index[1] = player_index[1] - 1
        matrix[player_index[1]][player_index[0]] = 2
    if key[pygame.K_DOWN]:
        matrix[player_index[1]][player_index[0]] = 0
        player_index[1] = player_index[1] + 1
        matrix[player_index[1]][player_index[0]] = 2

    return matrix, player_index

if __name__ == "__main__":
    size_x = 150
    size_y = 300
    elems = 1000

    screen = initDisplay([size_x, size_x])
    renderGrid(size_x, elems, True, screen)