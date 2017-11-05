grid = []
game = True # game loop

# create an empty grid
def init():
    for i in range(3):
        grid.append([])
        for j in range(3):
            grid[i].append('_')

# print the grid on screen
def affiche(grid):
    for j in ['A', 'B', 'C']:
        print('  ',j, sep=' ', end='  ')
    print('')
    for i in range(len(grid)):
        print(i+1, grid[i])

# check if the user input is valid
def casevide(grid, i, j):
    try:
        if grid[i][j] == '_':
            return True
        else:
            return False
    except IndexError:
        return 'wrong place'

# get the user input and place X on the location choosen by the user
# if the validation is OK
def choixjoueur(grid):
    choix = input('select a place ')
    [i,j] = choix
    i = int(i) - 1
    if j.lower() == 'a': j = 0
    elif j.lower() == 'b': j = 1
    elif j.lower() == 'c': j = 2
    else: j = 0
    print(i,j)
    if casevide(grid, i, j) == True:
        grid[i][j] = 'X'

def choixmachine(grid):
    import random as rd
    while True:
        i = rd.randint(0,3) # generate a random number for row
        j = rd.randint(0,3) # generate a random number for column
        if casevide(grid, i, j) == True:
            print(i,j)
            grid[i][j] = 'O'
            break

# check if the grid is full or not
def gridplein(grid):
    for i in range(len(grid)):
        if '_' in grid[i]:
            return False
    return True

def gagne(grid, char):
    

init()

#choixjoueur(grid)
for _ in range(15):
    choixmachine(grid)
    if gridplein(grid) == False:
        affiche(grid)
    else:
        affiche(grid)
        print('grid full')
        break
