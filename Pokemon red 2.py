





# adding random librarys

import random
import time






#variaibles                                                                                                                                                                                                                                                                                                                                                                                  what the epstein?
matrix = [{"thing":"other"},{"thing2","other2"}]

wild_pokemon = [
    {"Name":"Charizard","Type":"Fire","Level":random.randint(1,5),"Health":random.randint(50,100),"Attack":["Blaze",random.randrange(4,7), "Solar Beam", random.randrange(7,9)]}, #pokemon has name, type, health, and level in dictionary
    {"Name":"Vaporeon","Type":"Water","Level":random.randint(1,7),"Health":random.randint(10,30),"Attack":["brine",random.randrange(8,11), "rock smash", random.randrange(4,6)]},
    {"Name":"diglet","Type":"Earth","Level":random.randint(1,2),"Health":random.randint(7,24),"Attack":["spelunk",random.randrange(2,4), "mud slap", random.randrange(3,16)]},
    {"Name":"Raichu","Type":"Electric","Level":random.randint(1,3),"Health":random.randint(12,28),"Attack":["thunder shock",random.randrange(4,10), "pay day", random.randrange(3,5)]},
    {"Name":"Mr Mime","Type":"psychic","Level":random.randint(1,9),"Health":random.randint(15,40),"Attack":["happy mime",random.randrange(6,12), "double slap", random.randrange(2,18)]},
    {"Name":"Jigglypuff","Type":"Fiary","Level":random.randint(1,4),"Health":random.randint(35,68),"Attack":["sing",random.randrange(2,6), "double slap", random.randrange(10,12)]},
    {"Name":"Lopunny","Type":"Normal","Level":random.randint(1,10),"Health":random.randint(4,17),"Attack":["round",random.randrange(6,8), "hidden power", random.randrange(9,10)]},


]
my_pokemon = [
    {"Name":"venosaur","Type":"grass","Level":3,"Health":55,"Attack":["vine whip",random.randrange(4,7), "toxic", random.randrange(7,9)]},
    {"Name":"Lucario","Type":"normal","Level":4,"Health":32,"Attack":["Aqua Sphere",random.randrange(3,5), "High Jump Kick", random.randrange(6,10)]}
]

player_choose_move = True







#functions


def overworld_timer():
    timer = random.randint(0,0)
    print(timer)
    time.sleep(timer)
    print("battle start")
    battle()
def battle():
    wild_pokemon_number = random.randint(0,len(wild_pokemon)-1)
    pokemon = wild_pokemon[wild_pokemon_number]
    player_pokemon = my_pokemon[0]
    player_pokemon_hp = player_pokemon["Health"]


    #show player locaton

    print("player pokemon:",player_pokemon["Name"])
    print("Player pokemon hp:",player_pokemon_hp)

    #show enemy pokemon

    print("you encountered a wild",pokemon["Name"])
    print("its a",pokemon["Type"], "type pokemon")
    print("its level is",pokemon["Level"])
    print("it has",pokemon["Health"],"health")


    while True:
        wild_pokemon_attack = random.randint(0,len(wild_pokemon[wild_pokemon_number-1],2) #fix this
        print("enemy pokemon:",wild_pokemon[wild_pokemon_number]["Name"],"is using",wild_pokemon[wild_pokemon_number]["Attack"][wild_pokemon_attack])
        break

    while player_choose_move == True:
        print(my_pokemon[0],"has moves:",player_pokemon["Attack"])
        player_move = input("choose by typing move names")
        if player_move in player_pokemon["Attack"]:
            pokemon["Health"] = pokemon["Health"] - 7



#start codezxzxzxzxzzxzxzxzxzxz
overworld_timer()




































































