

board = [["","","","",""],
         ["","","","",""],
         ["","","","",""], #5x5 grid
         ["","","","",""],
         ["","","","",""]]






#---------------start code---------------


while True:
    player_1_placement_row = int(input("which row do you want to place your ship"))
    player_1_placement_column = int(input("which column do you place your ship in "))
    board[player_1_placement_row][player_1_placement_column] = "S1"
    player_1_placement_column += 1
    board[player_1_placement_row][player_1_placement_column] = "S1"
    
    for i in range(0,5):
        print(board[i])

