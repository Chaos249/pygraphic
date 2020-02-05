
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
    state = False
    point_count = 0

    for x in range(0, size):
        for y in range(0, size):
            elem = current_m[x][y]

            neighbors = 0
            neighbors_list = []

            neighbors, neighbors_list = countNeighbors(current_m, x, y)

            if elem == 3 and neighbors >= 1:
                for i in neighbors_list:
                    if i == 2:
                        matrix[x][y] = 0
                        point_count += 1
            elif elem == 2 and neighbors >= 1:
                for i in neighbors_list:
                    if i == 1:
                        state = True
            if elem == 0 and neighbors == 3:
                future_m[x][y] = 1
            elif elem == 1 and (neighbors < 2 or neighbors > 3):
                future_m[x][y] = 0
            else:
                future_m[x][y] = elem

    current_m = future_m
    return current_m, state, point_count

def initGameOfLife(size, elems):
    matrix = makeMatrix(size, size)
    matrix = populateMatrix(matrix, size, elems)
    return matrix

def populateMatrix(matrix, size, elems):
    for i in range(elems):
        matrix[random.randrange(0, size)][random.randrange(0, size)] = 1
    matrix[(size // 2) + 1][size // 2] = 0
    matrix[size // 2][(size // 2) + 1] = 0
    matrix[(size // 2) - 1][size // 2] = 0
    matrix[size // 2][(size // 2) - 1] = 0
    matrix[(size // 2) + 1][(size // 2) + 1] = 0
    matrix[(size // 2) - 1][(size // 2) - 1] = 0
    matrix[(size // 2) + 1][(size // 2) - 1] = 0
    matrix[(size // 2) - 1][(size // 2) + 1] = 0
    return matrix

def countNeighbors(matrix, x, y):
    count = 0
    neighbors_list = []
    try:
        if matrix[x + 1][y] == 1 or matrix[x + 1][y] == 3:
            count += 1
            neighbors_list.append(matrix[x + 1][y])
    except:
        pass
    try:
        if matrix[x + 1][y - 1] == 1 or matrix[x + 1][y - 1] == 3:
            count += 1
            neighbors_list.append(matrix[x + 1][y - 1])
    except:
        pass
    try:
        if matrix[x][y - 1] == 1 or matrix[x][y - 1] == 3:
            count += 1
            neighbors_list.append(matrix[x][y - 1])
    except:
        pass
    try:
        if matrix[x - 1][y - 1] == 1 or matrix[x - 1][y - 1] == 3:
            count += 1
            neighbors_list.append(matrix[x - 1][y - 1])
    except:
        pass
    try:
        if matrix[x - 1][y] == 1 or matrix[x - 1][y] == 3:
            count += 1
            neighbors_list.append(matrix[x - 1][y])
    except:
        pass
    try:
        if matrix[x - 1][y + 1] == 1 or matrix[x - 1][y + 1] == 3:
            count += 1
            neighbors_list.append(matrix[x - 1][y + 1])
    except:
        pass
    try:
        if matrix[x][y + 1] == 1 or matrix[x][y + 1] == 3:
            count += 1
            neighbors_list.append(matrix[x][y + 1])
    except:
        pass
    try:
        if matrix[x + 1][y + 1] == 1 or matrix[x + 1][y + 1] == 3:
            count += 1
            neighbors_list.append(matrix[x + 1][y + 1])
    except:
        pass
    return count, neighbors_list

def addMore(matrix, size):
    for i in range(size):
        matrix[0][i] = 1
    for i in range(size):
        matrix[-1][i] = 1
    for i in range(size):
        matrix[i][0] = 1
        matrix[i][-1] = 1
    return matrix

def addBoardPoints(matrix, size):
    matrix[random.randrange(0, size)][random.randrange(0, size)] = 3
    return matrix

def setCharacter(matrix, size):
    matrix[size//2][size//2] = 2
    player_index = [size//2, size//2]
    return player_index
