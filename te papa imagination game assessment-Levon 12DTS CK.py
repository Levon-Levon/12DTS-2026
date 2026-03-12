




#--------------------------library imports------------------
import time
import random







#-----------------------------variables-------------------------

class_type = []
inventory = []
honour = 0
resulting_honour = ""
honour_types = ["honourable","neutral","dishonourable"]
player_choosing = True


weapons = [
    {"name":"fist","damage":5,"type":":melee"},
    {"name":"sword","damage":13,"type":"melee"}


]

classes = [
    {"name":"bronie","strength":8,"charisma":3,"intelligence":9,"vigor":7,"smell":12,"luck":11,"street cred":2},
    {"name":"csgo try-hard","strength":6,"charisma":6,"intelligence":8,"vigor":8,"smell":11,"luck":6,"street cred":10},
    {"name":"prime shivam","strength":12,"charisma":10,"intelligence":6,"vigor":13,"smell":5,"luck":4,"street cred":6},
    {"name":"mr. E","strength":3,"charisma":12,"intelligence":11,"vigor":5,"smell":4,"luck":10,"street cred":12},


]

#--------------------------functions-----------------------------



def honour():
    global honour
    if honour < 0:
        resulting_honour = honour_types[2]

    elif 50> honour >= 0:
        resulting_honour = honour_types[1]
    elif honour >= 50:
        resulting_honour = honour_types[0]
    return resulting_honour

def character_choose():
    global class_type
    global class_area
    global player_choosing
    print(classes[class_area]["name"])
    end_loop = input("is that your selected class type? y or n")
    while True:
        if "y" in end_loop:
            class_type = classes[class_area]
            player_choosing = False
            return class_type
        elif "n" in end_loop:
            print("choose again")
            break
        else:
            print("invalid input try again")
def main_menu():




#----------------------------code------------------------

while True:
    while main_menu == True:
        try:
            player_option = int(input("type 1 to start game, type 2 to exit, type 3 for how to play"))
            if player_option == 1:
                print("you have started the game")
                break
            elif player_option == 2:
                quit()
            elif player_option == 3:
                print("this is a turn based combat adventure puzzle game which has you using your brain to get past all the obstacles")
                print("type locations to move to them, open inventory with i,")
            else:
                print("type a number from 1-3")
        except ValueError:
            print("not a valid input")


    print("")




    for i in range (0,len(classes)):
        print(classes[i])



    while player_choosing == True: #player selects class they play
        try:
           class_type = int(input("type the adjacent number of the class you want to play from 1-4"))
           if 4 >= class_type >=1: #checks if within boundry limits of 4 characters
               class_area = class_type - 1 #starts from 0 for computer checking within the dictionary in the function
               character_choose()
           else: #standard error and retrys loop
               print("type a number from 1-4")
        except ValueError: #if player didn't type an integer
            print("invalid input")







