# from typing import Counter

my_grid = [['x', 'o', '_'],['o', 'x', '_'],['_', 'o', 'x']]
ch = 'x'

my_grid1 = [['x', 'o', '_'],
           ['x', 'x', 'x'],
           ['_', 'o', '0']]

my_grid2 = [['o', 'x', '_'],
            ['o', 'x', '_'],
            ['_', 'x', 'o']]

my_grid3 = [['x', 'o', '_'],
           ['o', 'x', '_'],
           ['_', 'o', 'x']]

def checkTicTacTrue(matrix,c):
    """
    checking if "char" will win this game
    """
    result = 0
    if c in matrix[0]:
        for i in range(0,len(matrix)):
            if (matrix[i][0]  == matrix[i][1] == matrix[i][2]):
                result = 1
            if (i == 0):
                if (matrix[i][0] == matrix[i+1][1] == matrix[i+2][2]):
                    result = 1
                elif (matrix[i][2] == matrix[i+1][1] == matrix[[i+2][0]]):
                    result = 1
                elif (matrix[i][0] == matrix[i+1][0] == matrix[i+2][0]):
                    result = 1
                elif (matrix[i][1] == matrix[i+1][1] == matrix[i+2][1]):
                    result = 1
                elif (matrix[i][2] == matrix[i+1][2] == matrix[i+2][2]):
                    result = 1

    if result:
        return True
    else:
        return ("Not a win")

print(checkTicTacTrue(my_grid, ch))
print(checkTicTacTrue(my_grid1, ch))
print(checkTicTacTrue(my_grid2, ch))
print(checkTicTacTrue(my_grid3, ch))