from random import randint



hidden_pattern = [["  "] * 8 for x in range (8)]
guess_pattern = [["  "] * 8 for x in range (8)]
board_dimension = 8

let_to_num = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6, "H": 7}
make_ship = {"Aircraft Carrier": 5, "Battleship": 4, "Cruiser": 3, "Submarine": 3, "Destroyer": 2}

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
    for i,length in make_ship.items():         
        col = int(randint(0,7))
        row = int(randint(0,7))
        orientation_id = int(randint(0,1))
        if orientation_id == 0:
            orientation = "V"
        else:
            orientation = "H"
            if orientation == "V" and col+length > 8:
                print("The AI had placed a ship out of bounds")
            elif orientation == "H" and row+length > 8:
                print("The AI had placed a ship out of bounds")
            else:
                if orientation == "H":
                    for num in range(0,length):
                        if hidden_pattern[col-1][row+num] != " ":
                            print("The AI had placed a ship in another ship's way")
                elif orientation == "V":
                    for num in range(0,length):
                        if hidden_pattern[col-1+num][row] != " ":
                            print("The AI had placed a ship out of bounds")
                                
                for count in range(0,length):
                    if orientation == "H":
                        hidden_pattern[col-1][row+count] = i[0]
                    else:
                        hidden_pattern[col-1+count][row] = i[0]
                   
                break
        for j in range(length):
            board [row + i][col] = 1
        for k in range(length):
            board [row][col + i] = 1
        
      
def count_hit_ships(board):
    count=0
    for row in board:
        for column in row:
            if column=='X ':
                count+=1
    return count


#print_board(hidden_pattern)
turns = 100

    
while turns > 0:
    print('Welcome to Battleship')
    print_board(guess_pattern)
    create_ships(hidden_pattern)
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
    if count_hit_ships(guess_pattern) == 5:
        print("Congratulations you have sunk all the battleships ")
        break
    print(' You have ' +str(turns) + ' turns remaining ')
    if turns == 0:
        print('Game Over ')
        break
