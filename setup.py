import conway

import pygame
pygame.init()


SIZE = WIDTH, HEIGHT = (550, 450)
FPS = 30
screen = pygame.display.set_mode(SIZE, pygame.RESIZABLE)
clock = pygame.time.Clock()


def blit_text(surface, text, pos, font, color=pygame.Color('white')):
    words = [word.split(' ') for word in text.splitlines()]  # 2D array where each row is a list of words.
    space = font.size(' ')[0]  # The width of a space.
    max_width, max_height = surface.get_size()
    x, y = pos
    for line in words:
        for word in line:
            word_surface = font.render(word, 0, color)
            word_width, word_height = word_surface.get_size()
            if x + word_width >= max_width:
                x = pos[0]  # Reset the x.
                y += word_height  # Start on new row.
            surface.blit(word_surface, (x, y))
            x += word_width + space
        x = pos[0]  # Reset the x.
        y += word_height  # Start on new row.


size = 80
elems = 2500
matrix = conway.initGameOfLife(size, elems)

font = pygame.font.SysFont('Arial', 4)

while True:
    dt = clock.tick(FPS) / 1000

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()

    matrix = conway.gameOfLife(matrix, size, elems)
    m_string = conway.prettyPrint(matrix)
    text = m_string
    screen.fill((10, 10, 10))
    blit_text(screen, text, (20, 20), font)
    pygame.display.update()