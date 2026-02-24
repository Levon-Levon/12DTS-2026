



board = [["_","_","_"],
         ["_","_","_"], #basic board creation
         ["_","_","_"]
         ]

list_amount_column = []
column_number = 0
row_number = 0
sum_column = 0 #defining start variables
win = False



def move(player_thing):
    while True:
        print(player_thing)
        if player_thing == "X":
           board_placement_row_X = int(input("which row do you place x in?"))  # placing X for first then second brackets
           board_placement_column_X = int(input("which column do you place x in?"))
           board_placement_column_X -= 1
           board_placement_row_X -= 1  # making placements align with player expectaions by removing the "0"


           if board[board_placement_column_X][board_placement_row_X] == "_":
                board[board_placement_column_X][board_placement_row_X] = "X"
                break
           else:
                print("that is an occupied space try again")


        else:
           board_placement_row_O = int(input("which row do you place O in?"))
           board_placement_column_O = int(input("which row do you place O in?"))
           board_placement_column_O -= 1
           board_placement_row_O -= 1

           if board[board_placement_column_O][board_placement_row_O] == "_":
               board[board_placement_column_O][board_placement_row_O] = "O"
               break
           else:
               print("that is an occupied space try again")
    for i in range(0,3):
        print(board[i])








def winning_possibilites():
    print("doing function: winning_possiblilites") #check 8 possible wins in this function for winning check
    win = False

    column_number = 0
    row_number = 0
    sum_column = 0
    if board[0][0] == "X" and board[1][0] == "X" and board[2][0] == "X": #vertical x win first row
        win = True

    if board[0][1] =="X" and board[1][1] =="X" and board[2][1] == "X":#vertical X win second row
        win = True

    if board[0][2] == "X" and board[1][2] == "X" and board[2][2] == "X": #vertical X win thrid row
        win = True

    if board[0][0] == "X" and board[0][1] == "X" and board[0][2] == "X": #horizontal X win first row
        win = True

    if board[1][0] == "X" and board[1][1] == "X" and board[1][2] == "X": #horizontal X win second row
        win = True

    if board[2][0] == "X" and board[2][1] == "X" and board[2][2] == "X": #vertical X win thrid row
        win = True

    if board[0][0] == "X" and board[1][1] == "X" and board[2][2] == "X": #horizontal left up to right
        win = True

    elif board[2][0] == "X" and board[1][1] == "X" and board[0][2] == "X": #vertical X win thrid row
        win = True





    if win == True:
        print("you win")
    else:
        print()


while True:
    column_number = 0 #reset variables
    row_number = 0
    sum_column = 0


    move("X")
    winning_possibilites()
    move("O")
    winning_possibilites()

