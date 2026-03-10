import random

player_board = [["","","","",""],
         ["","","","",""],
         ["","","","",""], #5x5 grid
         ["","","","",""],
         ["","","","",""]]

player_hit_reference_board = [["","","","",""],
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
bot_striking = True
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






    while playing game == True: #repeats bots and players turns until someone's ships are destroyed
        for i in range(0,5): #below lines (63-78) are player choosing where to strike and checking if that spot is an enemy ship
            print(player_board[i])
        player_strike_row = int(input("which row do you want to strike the enemy ship")) # will replace the target with an "X"
        player_strike_column= int(input("which row do you want to strike the enemy ship"))# If the bot's "S1's" are gone then player wins, and vice versa.


        if bot_board[player_strike_row][player_strike_column] == "S1":
            bot_board[player_strike_row][player_strike_column] = "" # D is for destroy, M is for miss. Replaces
            player_hit_reference_board[player_strike_row][player_strike_column] = "D"
            print("hit clanker ship")
            for i in range(0,5):
                print(player_hit_reference_board[i])
        else:
            bot_board[player_strike_row][player_strike_column] = ""
            player_hit_reference_board[player_strike_row][player_strike_column] = "M"
            print("missed")


        while bot_striking == True: #bot using random inputs to hit ship, if it has hit a spot already and it was miss or hit it keeps going until finding a correct spot.
            bot_strike_row = random.randint(0,4)
            bot_strike_column = random.randint(0,4)
            if player_board[bot_strike_row][bot_strike_column] == "S1":
                print("bot hit your ship at")
                player_board[bot_strike_row][bot_strike_column] = "D"
                break
            elif player_board[bot_strike_row][bot_strike_column] == "M" or player_board[bot_strike_row][bot_strike_column] == "D":
                print( ) #retry loop is already stricken in that spot
            else:
                player_board[bot_strike_row][bot_strike_column] = "M"
                print("bot missed")
                break


