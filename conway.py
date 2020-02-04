
from prettytable import PrettyTable

import random

# Pure garbage funcitons
def makeMatrix(x_size, y_size):
    ptui_matrix = []
    for x in range(x_size):
        x_idx = []
        for y in range(y_size):
            x_idx.append(0)
        ptui_matrix.append(x_idx)
    return ptui_matrix

def prettyPrint(matrix):
    p = PrettyTable()
    for row in matrix:
        p.add_row(row)
    return p.get_string(header = False, border = False)

# Big boy shit
def gameOfLife(matrix, size):
    current_m = matrix
    future_m = makeMatrix(size, size)
    state = True

    for x in range(0, size):
        for y in range(0, size):
            elem = current_m[x][y]
            neighbors = countNeighbors(current_m, x, y)

            if elem == 2:
                return False
            if elem == 0 and neighbors == 3:
                future_m[x][y] = 1
            elif elem == 1 and (neighbors < 2 or neighbors > 3):
                future_m[x][y] = 0
            else:
                future_m[x][y] = elem

    current_m = future_m
    return current_m, state

def initGameOfLife(size, elems):
    matrix = makeMatrix(size, size)
    matrix = populateMatrix(matrix, size, elems)
    return matrix

def populateMatrix(matrix, size, elems):
    for i in range(elems):
        matrix[random.randrange(0, size)][random.randrange(0, size)] = 1
    return matrix

def countNeighbors(matrix, x, y):
    count = 0
    try:
        if matrix[x + 1][y] == 1:
            count += 1
    except:
        pass
    try:
        if matrix[x + 1][y - 1] == 1:
            count += 1
    except:
        pass
    try:
        if matrix[x][y - 1] == 1:
            count += 1
    except:
        pass
    try:
        if matrix[x - 1][y - 1] == 1:
            count += 1
    except:
        pass
    try:
        if matrix[x - 1][y] == 1:
            count += 1
    except:
        pass
    try:
        if matrix[x - 1][y + 1] == 1:
            count += 1
    except:
        pass
    try:
        if matrix[x][y + 1] == 1:
            count += 1
    except:
        pass
    try:
        if matrix[x + 1][y + 1] == 1:
            count += 1
    except:
        pass
    return count

def addMore(matrix, size):
    for i in range(size):
        matrix[0][i] = 1
        #matrix[1][i] = 1
    for i in range(size):
        matrix[-1][i] = 1
        #matrix[-2][i] = 1
    for i in range(size):
        matrix[i][0] = 1
        #matrix[i][1] = 1
        matrix[i][-1] = 1
        #matrix[i][-2] = 1
    return matrix

def setCharacter(matrix, size):
    matrix[size//2][size//2] = 2
    player_index = [size//2, size//2]
    return player_index


