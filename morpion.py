grid = []

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
        return False

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
    else:
        print('wrong place, choose again')
        choixjoueur(grid)

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

# check the grid for winner every turn
# compare each point in the grid to the points next to it
# if the points has the same X or O then declare winner and exit
def winner(grid, char):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            # check for horizantal alignement (X-X-X or O-O-O)
            if j == 0:
                if char == grid[i][j] and char == grid[i][j+1] and char == grid[i][j+2]:
                    return True
            if j == 1:
                if char == grid[i][j] and char == grid[i][j-1] and char == grid[i][j+1]:
                    return True
            if j == 1:
                if char == grid[i][j] and char == grid[i][j-1] and char == grid[i][j-2]:
                    return True
        # check for vertical alignement
        # X or O
        # X or O
        # X or O
        if i == 0:
            if char == grid[i] and char == grid[i+1] and char == grid[i+2]:
                return True
        if i == 1:
            if char == grid[i] and char == grid[i-1] and char == grid[i+1]:
                return True
        if i == 1:
            if char == grid[i] and char == grid[i-1] and char == grid[i-2]:
                True

init()

while True:
    choixjoueur(grid)
    
    if winner(grid, 'X') == True:
        affiche(grid)
        print('Winner => user')
        break
    choixmachine(grid)
    if gridplein(grid) == False:
        if winner(grid, 'O') == True:
            print('Winner => computer')
            break
        affiche(grid)
    else:
        affiche(grid)
        print('No Winner')
        break
