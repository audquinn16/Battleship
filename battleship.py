from random import randint

hidden_pattern = [["  "] * 8 for x in range (8)]
guess_pattern = [["  "] * 8 for x in range (8)]

let_to_num = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6, "H": 7}

def print_board(board):
    print('  A  B  C  D  E  F  G  H')
    print(' * * * * * * * * * * * * *')
    row_num=1
    for row in board:
        print("%d|%s|" % (row_num, "|".join(row)))
        row_num +=1
        
def get_ship_location():
    #Enter the row number between 1-8
    row=input('Please enter a ship row 1-8 ').upper()
    while row not in '12345678':
        print("Please enter a valid row ")
        row=input('Please enter a ship row 1-8 ')
    #Enter the Ship column from A-H
    column=input('Please enter a ship column A-H ').upper()
    while column not in 'ABCDEFGH':
        print("Please enter a valid column ")
        column=input('Please enter a ship column A-H ')
    return int(row)-1,let_to_num[column]

    
#Function that creates the ships
def create_ships(board):
    for ship in range(5):
        ship_r, ship_cl=randint(0,7), randint(0,7)
        while board[ship_r][ship_cl] =='X ':
            ship_r, ship_cl = randint(0, 7), randint(0, 7)
        board[ship_r][ship_cl] = 'X '
        
def count_hit_ships(board):
    count=0
    for row in board:
        for column in row:
            if column=='X ':
                count+=1
    return count

create_ships(hidden_pattern)
#print_board(hidden_pattern)
turns = 20
while turns > 0:
    print('Welcome to Battleship')
    print_board(guess_pattern)
    row,column =get_ship_location()
    if guess_pattern[row][column] == '-':
        print(' You already guessed that ')
    elif hidden_pattern[row][column] =='X ':
        print(' Congratulations you have hit the battleship ')
        guess_pattern[row][column] = 'X '
        turns -= 1
    else:
        print('Sorry,You missed')
        guess_pattern[row][column] = '- '
        turns -= 1
    if  count_hit_ships(guess_pattern) == 5:
        print("Congratulations you have sunk all the battleships ")
        break
    print(' You have ' +str(turns) + ' turns remaining ')
    if turns == 0:
        print('Game Over ')
        break


#https://gist.github.com/w0300133/7f3e3e6f836e519f64272150ca34080c
    #what i need to do from here: figure out how to make ships more than 1 space!