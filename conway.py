
from prettytable import PrettyTable

#Pure garbage funcitons
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
    print(p.get_string(header = False, border = False))

#Big boy shit
def life_game(currrent_m, size):

    #impl help : https://www.geeksforgeeks.org/program-for-conways-game-of-life/

    while True:
        future_m = makeMatrix(size, size)
        prettyPrint(future_m)
    return False

if __name__ == "__main__":
    size = 5
    m = makeMatrix(size, size)
    life_game(m, size)

    #test fuck
    """
    m = makeMatrix(25, 25)
    prettyPrint(m)"""

