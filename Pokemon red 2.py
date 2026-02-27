# adding random librarys

import random
import time
#variaibles
matrix = [{"thing":"other"},{"thing2","other2"}]

wild_pokemon = [
    {"Name":"Charizard","Type":"Fire","Level":random.randint(1,5),"Health":random.randint(50,100),"Attack":["Blaze",random.randrange(4,7), "Solar Beam", random.randrange(7,9)]}, #pokemon has name, type, health, and level in dictionary
    {"Name":"Vaporeon","Type":"Water","Level":random.randint(1,7),"Health":random.randint(10,30),"Attack":["scold",random.randrange(9,14), "rock smash", random.randrange(4,6)]},
    {"Name":"diglet","Type":"Earth","Level":random.randint(1,2),"Health":random.randint(7,24)},
    {"Name":"Raichu","Type":"Electric","Level":random.randint(1,3),"Health":random.randint(12,28)},
    {"Name":"Mr Mime","Type":"psychic","Level":random.randint(1,9),"Health":random.randint(15,40)},
    {"Name":"Jigglypuff","Type":"Fiary","Level":random.randint(1,4),"Health":random.randint(35,68)},
    {"Name":"Lopunny","Type":"Normal","Level":random.randint(1,10),"Health":random.randint(4,17)},


]

#functions


def overworld_timer():
    timer = random.randint(1,5)
    print(timer)
    time.sleep(timer)
    print("battle start")
    battle()
def battle():
    x = random.randint(0,len(wild_pokemon)-1)
    pokemon = wild_pokemon[x]
    print("you encountered a wild",pokemon["Name"])
    print("its a",pokemon["Type"], "type pokemon")
    print("its level is",pokemon["Level"])
    print("it has",pokemon["Health"],"health")




overworld_timer()




































































