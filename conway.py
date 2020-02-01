
from prettytable import PrettyTable

import random

# Pure garbage funcitons
def makeMatrix(x_size, y_size):
    ptui_matrix = []
    for x in range(x_size):
        x_idx = []
        for y in range(y_size):
            x_idx.append("")
        ptui_matrix.append(x_idx)
    return ptui_matrix

def prettyPrint(matrix):
    p = PrettyTable()
    for row in matrix:
        p.add_row(row)
    return p.get_string(header = False, border = False)

# Big boy shit
def gameOfLife(size, elems):
    current_m = makeMatrix(size, size)
    current_m = populateMatrix(current_m, size, elems)

    future_m = makeMatrix(size, size)

    for x in range(0, size):
        for y in range(0, size):
            elem = current_m[x][y]
            neighbors = countNeighbors(current_m, x, y)

            if elem == "" and neighbors == 3:
                future_m[x][y] = "■"
            elif elem == "■" and (neighbors < 2 or neighbors > 3):
                future_m[x][y] = ""
            else:
                future_m[x][y] = elem

    current_m = future_m

    # prettyPrint(current_m)

    return current_m

def countNeighbors(matrix, x, y):
    count = 0
    try:
        if matrix[x + 1][y] != "":
            count += 1
    except:
        pass
    try:
        if matrix[x + 1][y - 1] != "":
            count += 1
    except:
        pass
    try:
        if matrix[x][y - 1] != "":
            count += 1
    except:
        pass
    try:
        if matrix[x - 1][y - 1] != "":
            count += 1
    except:
        pass
    try:
        if matrix[x - 1][y] != "":
            count += 1
    except:
        pass
    try:
        if matrix[x - 1][y + 1] != "":
            count += 1
    except:
        pass
    try:
        if matrix[x][y + 1] != "":
            count += 1
    except:
        pass
    try:
        if matrix[x + 1][y + 1] != "":
            count += 1
    except:
        pass
    return count

def populateMatrix(matrix, size, elems):
    for i in range(elems):
        matrix[random.randrange(0, size)][random.randrange(0, size)] = "■"
    return matrix

"""if __name__ == "__main__":
    gameOfLife(25, 150)"""

    # test fuck
