





#--------------------------library imports------------------
import time
import random







#-----------------------------variables-------------------------




class_type = []
inventory = []
honour = 0
vending_machine_health = 20
resulting_honour = ""
honour_types = ["honourable","neutral","dishonourable"]
player_choosing = True
vending_machine = True
phase_one = True
phase_two = False
phase_three = False
success = "adsfasd"



equipment = {"headgear":"","body":"","leggings":"","feet":""}

classes = [
    {"name":"bronie","stats":["strength",8,"charisma",3,"intelligence",9,"vigor",7,"smell",12,"luck",11,"street cred",2,"cash",12]},
    {"name":"csgo try-hard","stats":["strength",6,"charisma",6,"intelligence",8,"vigor",8,"smell",11,"luck",6,"street cred",10,"cash",5]},
    {"name":"prime shivam","stats":["strength",12,"charisma",10,"intelligence",6,"vigor",13,"smell",5,"luck",4,"street cred",6,"cash",8]},
    {"name":"mr. E","stats":["strength",3,"charisma",12,"intelligence",11,"vigor",5,"smell",4,"luck",10,"street cred",12,"cash",24]},


]

encounter_messages = ["do you want to quit the game? type 1 if you do, type 2 to keep playing.",
                      "you encounter a redditor, type 1 to punch his groin, type 2 to flex reddit karma, type 3 to flex reddit gold",
                      "you are at a vending machine, type 1 to kick machine, type 2 to purchase soda pop for $5",





                      ]
encounters = ["redditor","vending machine","asdfasdf"]

#--------------------------functions-----------------------------

def skill_check_encounter(encounter_decider):
    global inventory
    global vending_machine_health # i might not need to global since these only exist within function?
    global vending_machine
    global success

    print(encounter_messages[encounter_decider]) #saves typing multiple prints for each encounter by recieveing message from list
    amount_stat_needed = random.randint(0,20)  # rolls an imaginary D20 and if your stat is higher, then you beat encounter.
    for i in range(0, len(classes[class_area]["stats"]), 2):  # this loop shows all player stats so they can decide which is best to counter the scenario
        print(classes[class_area]["stats"][i], " = ", classes[class_area]["stats"][i + 1]) #gets first element of  stats list in player dictionary, then visually shows it equal to the next element
    if encounter_decider == 0: #the quitting scenario, always available
       while True:
           try:
                scenario_chosen = int(input(""))
                if scenario_chosen == 1:
                    quit()
                elif scenario_chosen == 2:
                    print("you have chosen to keep playing")
                    break
                else:
                    print("not a number from 1-2")
           except ValueError:
               print("not a valid input")


    if encounter_decider == 1: #corresponding from list
        while True:
            try:
                scenario_chosen = int(input("choose which scenario to counter"))

                if scenario_chosen == 1:
                    amount_stat_needed = 99
                    print("required strength is: ", amount_stat_needed)
                    if classes[class_area]["stats"][1] >= amount_stat_needed:
                        print("you successfully punch the redditor, you gain +1 strength")
                        classes[class_area]["stats"][1] += 1
                        success = "y"
                    else:
                        print("your fist bounced off his stomach and hit your face, you lose 1 strength")
                        classes[class_area]["stats"][1] -= 1
                    break

                elif scenario_chosen == 2:
                    amount_stat_needed += 2
                    print("required street cred is: ", amount_stat_needed)
                    if classes[class_area]["stats"][13] >= amount_stat_needed:
                        print("your reddit karma obliviates the redditor, you gain +1 street cred")
                    else:
                        print("your karma is lower than his (you should post more memes bro), you lose 1 street cred")
                        classes[class_area]["stats"][13] -= 1
                    break
                elif scenario_chosen == 3:
                    amount_stat_needed -= 7
                    print("required luck is: ", amount_stat_needed)
                    if classes[class_area]["stats"][11] >= amount_stat_needed:
                        print("your golden soul blesses him, you gain +1 luck and he gives you 1 dollar")
                        classes[class_area]["stats"][11] += 1
                        classes[class_area]["stats"][15] += 1
                    else:
                        print("his gold overwhelms you, you lose 1 dollar for each subreddit this guy moderates (9)")
                        classes[class_area]["stats"][15] -= 9
                    break
                else:
                    print("type a number from 1-3")

            except ValueError:
                print("not a number try again")




    elif encounter_decider == 2: #vending machine scenario
        if vending_machine == True: #if vending machine hasn't been broken by previous actions
            while True:
                try:
                    scenario_chosen = int(input("choose which scenario to counter"))
                    if scenario_chosen == 1:
                        vending_machine_health -= 2
                        print("you kick the vending machine...")
                        amount_stat_needed += 1
                        print("required luck is: ", amount_stat_needed)
                        time.sleep(1)
                        if classes[class_area]["stats"][1] >= amount_stat_needed:
                            print("you successfully extract a can of soda, the vending machine looks a bit damaged though...")
                            vending_machine_break = random.randint(0,vending_machine_health) #picks from 0- whatever the health has become, if 0 then permanent destruction
                            if vending_machine_break <= 0:
                                print("the vending machine has been permanently destroyed...")
                                vending_machine = False

                            inventory.append("soda")
                        else:
                            print("your foot hurts and the vending machine is now damaged and angry >:(, you lose 2 dollars and 1 strength")
                            classes[class_area]["stats"][1] -= 1
                            classes[class_area]["stats"][15] -= 2
                        break

                    elif scenario_chosen == 2:
                        print("you test your luck to buy a soda pop...")
                        amount_stat_needed -= 6
                        print("required luck is: ",amount_stat_needed)
                        time.sleep(1)
                        if classes[class_area]["stats"][11] >= amount_stat_needed:
                            print("you successfully buy a soda pop, you lose 5 dollars though...")
                            inventory.append("soda")
                            classes[class_area]["stats"][11] -= 5
                        else:
                            print("soda got stuck when falling, you bash your head in anger and lose intelligence on top of your money (vending machine gets damaged too)")
                            vending_machine_health -= 1
                            classes[class_area]["stats"][5] -=1
                            classes[class_area]["stats"][15] -= 5
                        break

                    else:
                        print("type a number from 1-2")


                except ValueError:
                    print("type a valid number")
                break
        else:
            print("the vending machine was broken")







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
    global player_choosing
    global class_area
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
            break





#----------------------------code------------------------

while True:
    while True:
        try:
            player_option = int(input("type 1 to start game, type 2 to exit, type 3 for how to play"))
            if player_option == 1:
                print("you have started the game")
                break
            elif player_option == 2:
                print("goodbye!")
                quit()
            elif player_option == 3:
                print("this is an adventure dnd inspired puzzle game which has you using your brain (and rng) to get past all the obstacles")
                time.sleep(2)
                print("type the first letter as indicated in [] to move to/do a scenario")
                time.sleep(2)
                print("you lose the game if any stat (including cash) is reduced to zero or lower")
            else:
                print("type a number from 1-3")
        except ValueError:
            print("not a valid input")


    print("Some guy that insulted your reddit account turned out to be the ceo of your favourite fast-food chain glorbguck inc. ")
    print("your goal is to break into his large epic skyscraper and humiliate him in the most gratifying way you can imagine.")
    print("but first, you must pick your angry redditor")




    while player_choosing == True: #player selects class they play
        for i in range(0, len(classes)):
            print(classes[i]["name"], "=", i+1 )#accesses names from dictionary and prints from the range of 0-3

        try:
           class_type = int(input("type the adjacent number of the class you want to play from 1-4"))
           if 4 >= class_type >=1: #checks if within boundry limits of 4 characters
               class_area = class_type - 1 #starts from 0 for computer checking within the dictionary in the function
               character_choose()
           else: #standard error and retrys loop
               print("type a number from 1-4")
        except ValueError: #if player didn't type an integer
            print("invalid input")


    while True:
        while phase_one == True: #start here but player could go to many different points of the game, all phases start out false and certain ones will be unlocked based on specific scenario
            chosen_area = input("you stand at the front gates of the large corporate building, you notice a [v]ending machine,the [f]ront gates, and a [m]ouldy piece of cheese on the ground. ")
            if chosen_area == "v":
                encounter_decider = 2
                skill_check_encounter(encounter_decider)

            elif chosen_area == "f":
                print()

            elif chosen_area == "m": # mouldy cheese path for phase 1
                print("you pick up the mouldy cheese and place it in your inventory, you seem to be a little stinkier then before...")
                classes[class_area]["stats"][9] += 1
                chosen_area = input("as you stuff the cheese in you pocket you notice an entrance by the right side door, but a fat guard is blocking your path, [s]neak, [c]onfront")
                if chosen_area == "s":
                    print()

                elif chosen_area == "c":
                    encounter_decider = 1
                    success = ""
                    skill_check_encounter(encounter_decider)
                    print(success)
                    if success == "y":
                        print("you have entered the building, the outside now does not exist")

                    else:
                        print("you failed confronting the redditor, you still enter the right side but must now wear the badge of shame permanently")
                        equipment["headgear"] = "badge of shame"
                        print(equipment["headgear"])
                    phase_one = False
                    phase_three = True

        while phase_two == True:
            asdfasdf = input("")

        while phase_three == True:
            print("")

























