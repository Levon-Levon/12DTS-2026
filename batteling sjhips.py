import random

player_board = [["","","","",""],
         ["","","","",""],
         ["","","","",""], #5x5 grid
         ["","","","",""],
         ["","","","",""]]


bot_board = [["","","","",""],
         ["","","","",""],
         ["","","","",""], #5x5 grid
         ["","","","",""],
         ["","","","",""]]



player_1_placement = True
bot_placement = True
#---------------start code---------------


while True:



    while bot_placement == True:
        bot_placement_row = random.randint(0,3) #bot's ship is placed in a random possible spot
        bot_placement_column = random.randint(0,3)
        bot_board[bot_placement_row][bot_placement_column] = "S1"
        bot_placement_column += 1
        bot_board[bot_placement_row][bot_placement_column] = "S1"
        bot_placement = False
    for i in range(0,5):
        print(bot_board[i])

    while player_1_placement == True:  # places ships and makes sure that there's no out of range placements
        player_1_placement_row = int(input("which row do you want to place your ship"))
        player_1_placement_column = int(input("which column do you place your ship in "))
        if player_1_placement_row < 4:  # if the 2-1 ship is going to go out of range

            player_board[player_1_placement_row][player_1_placement_column] = "S1"
            next_placement = True
            player_1_placement_column += 1
            player_board[player_1_placement_row][player_1_placement_column] = "S1"
            break

        else:
            print("placement outside of board try again")







    for i in range(0,5):
        print(player_board[i])
    player_strike_row = int(input("which row do you want to strike the enemy ship")) # will replace the target with an "X"
    player_strike_column= int(input("which row do you want to strike the enemy ship"))# If the bot's "S1's" are gone then player wins, and vice versa.


    if player_board[player_strike_row][player_strike_column] == "S1":
        bot_board[player_strike_row][player_strike_column] = "D" # D is for destroy, M is for miss
        print("hit clanker ship")
    else:
        bot_board[player_strike_row][player_strike_column] = "M"
        print("missed")
