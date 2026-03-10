



#--------------------------library imports------------------
import time
import random







#-----------------------------variables-------------------------


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
    end_loop = input("is",classes[class_area]["name"] ,  " your selected class type? yes or no")
    if "y" in end_loop:
        class_type = classes[class_area]
        return class_type
    elif "n" in end_loop:
        print("choose again")
    else:
        print("invalid input try again")



#----------------------------code------------------------

while True:
    print("hi")

    for i in range (0,len(classes)):
        print(classes[i])



    while player_choosing == True: #player selects class they play
        try:
           class_type = str(input("type the name of the class you want to play"))


           if "b" in class_type: #checks for bronie class since only b in this class
               class_area = 0
               character_choose()


           elif "c" in class_type:
               class_area = 1



        except:
            print("invalid input")
























































