



#--------------------------library imports------------------
import time
import random







#-----------------------------variables-------------------------


inventory = []
honour = 0
resulting_honour = ""
honour_types = ["honourable","neutral","dishonourable"]



weapons = [
    {"name":"fist","damage":5,"type":":melee"},
    {"name":"sword","damage":13,"type":"melee"}


]

classes = [
    {"name":"furry","strength":8,"charisma":3,"intelligence":9,"vigor":7,"smell":12,"luck":11,"epicness":2},
    {"name":"csgo try-hard","strength":4,"charisma":4,"intelligence":8,"vigor":12,"smell":11,"luck":6,"epicness":10},
    S


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




#----------------------------code------------------------

while True:
    print("hi")

    for i in range (0,len(classes))
        print(classes[i])































































