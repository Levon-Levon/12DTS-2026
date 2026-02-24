

board = [["","","","",""],
         ["","","","",""],
         ["","","","",""], #5x5 grid
         ["","","","",""],
         ["","","","",""]]




player_1_placement = True

#---------------start code---------------


while True:
    player_1_placement_row = int(input("which row do you want to place your ship"))
    player_1_placement_column = int(input("which column do you place your ship in "))

    while player_1_placement == True:
        if player_1_placement_row <=4:
            try:
                board[player_1_placement_row][player_1_placement_column] = "S1"
                next_placement = True
            except:
                print("placement outside of board try again")
                break
        if next_placement == True:
            try:
                player_1_placement_column += 1
                board[player_1_placement_row][player_1_placement_column] = "S1"
                break
            except:
                print("placement outside of board try again")
                break



    for i in range(0,5):
        print(board[i])

