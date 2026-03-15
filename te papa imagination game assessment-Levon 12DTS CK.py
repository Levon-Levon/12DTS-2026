





#--------------------------library imports------------------
import time
import random







#-----------------------------variables-------------------------

inventory = ["grenade","katana"]
vending_machine_health = 20
vending_machine = True
difficulty = 0

player_choosing = True

phase_one = True
phase_two = False
phase_three = False
success = ""

list_for_gaining_stats = [1,3,5,7,9,11,13,15] #probably not efficient but helps when wanting to decrease or increase a certain stat, especially when randomizing

classes = [
    {"name":"bronie","stats":["strength",88,"charisma",3,"intelligence",9,"vigor",7,"smell",12,"luck",11,"street cred",2,"cash",14]}, # has all necesseray valus for player
    {"name":"csgo try-hard","stats":["strength",6,"charisma",6,"intelligence",8,"vigor",8,"smell",11,"luck",6,"street cred",10,"cash",6]},
    {"name":"prime shivam","stats":["strength",12,"charisma",10,"intelligence",6,"vigor",13,"smell",5,"luck",4,"street cred",6,"cash",10]},
    {"name":"mr. E","stats":["strength",3,"charisma",12,"intelligence",11,"vigor",5,"smell",4,"luck",10,"street cred",12,"cash",21]},


]
ENCOUNTER_MESSAGES = ["", #messages correspond to each scenario, first message is blank for when checking if a stat has gone below zero or not
                      "do you want to quit the game? type 1 if you do, type 2 to keep playing.",
                      "you encounter a redditor, type 1 to punch his groin, type 2 to flex reddit karma, type 3 to flex reddit gold",
                      "you are at a vending machine, type 1 to kick machine, type 2 to purchase soda pop for $5",]

#--------------------------functions-----------------------------


def skill_check_encounter(encounter_decider,difficulty):#parameters encounter decider is for which scenario they do, difficulty is influenced by how they got there.
    global inventory
    global vending_machine_health # i might not need to global since these only exist within function?
    global vending_machine
    global success

    print(ENCOUNTER_MESSAGES[encounter_decider]) #saves typing multiple prints for each encounter by recieveing message from list
    amount_stat_needed = random.randint(0,20)  # rolls an imaginary D20 and if your stat is higher, then you beat encounter.
    for i in range(0, len(classes[class_area]["stats"]), 2):  # this loop shows all player stats so they can decide which is best to counter the scenario
        print(classes[class_area]["stats"][i], " = ", classes[class_area]["stats"][i + 1]) #gets first element of  stats list in player dictionary, then visually shows it equal to the next element

    if encounter_decider == 0:
        print()

    if encounter_decider == 1: #the quitting scenario, always available
       while True: #repeats specific scenario until valid outcome has been reached
           try:
                scenario_chosen = int(input("")) #each scenario will have multiple outcomes so loop and try and except is neccecery for the multiple outcomes
                if scenario_chosen == 1: #if valid inputs the 1 and 2 do their correct corresponding actions
                    print("goodbye!")
                    quit()
                elif scenario_chosen == 2:
                    print("you have chosen to keep playing")
                    break
                else:
                    print("not a number from 1-2") #checks for valid input
           except ValueError:
               print("not a valid input") #checks for valid input

    elif encounter_decider == 2: #corresponding from list
        while True:
            try:
                scenario_chosen = int(input("choose which scenario to counter"))

                if scenario_chosen == 1:
                    print("you try to punch the redditor") #prints your attempted action for added clarity
                    amount_stat_needed += difficulty #based on assumed "difficulty" of encounter required stats will be decreased for ease
                    print("required strength is: ", amount_stat_needed)  #shows player required stat before ending encounter
                    time.sleep(2)
                    if classes[class_area]["stats"][1] >= amount_stat_needed: #if stat is equal to or greater required then player is rewarded
                        print("you successfully punch the redditor, you gain +1 strength")
                        classes[class_area]["stats"][1] += 1
                        success = "y" #extra global output variable "success" which could potentially be used for deciding ventures for the player
                    else:
                        print("your fist bounced off his stomach and hit your face, you lose 1 strength") #if lower than player is punished
                        classes[class_area]["stats"][1] -= 1
                    break

                elif scenario_chosen == 2:
                    amount_stat_needed += difficulty
                    print("required street cred is: ", amount_stat_needed)
                    if classes[class_area]["stats"][13] >= amount_stat_needed:
                        print("your reddit karma obliviates the redditor, you gain +1 street cred")
                    else:
                        print("your karma is lower than his (you should post more memes bro), you lose 1 street cred")
                        classes[class_area]["stats"][13] -= 1
                    break
                elif scenario_chosen == 3:
                    difficulty -= 7
                    amount_stat_needed += difficulty
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




    elif encounter_decider == 3: #vending machine scenario
        if vending_machine == True: #if vending machine hasn't been broken by previous actions
            while True:
                try:
                    scenario_chosen = int(input("choose which scenario to counter")) #choosing scenario
                    if scenario_chosen == 1:
                        vending_machine_health -= 2
                        print("you kick the vending machine...")
                        amount_stat_needed += difficulty
                        print("required luck is: ", amount_stat_needed)
                        time.sleep(1)
                        if classes[class_area]["stats"][1] >= amount_stat_needed:
                            print("you successfully extract a can of soda, the vending machine looks a bit damaged though...")
                            vending_machine_health -= 2
                            inventory.append("soda")
                        else:
                            print("your foot hurts and the vending machine is now damaged and angry >:(, you lose 2 dollars and 1 strength")
                            vending_machine_health -= 1
                            classes[class_area]["stats"][1] -= 1
                            classes[class_area]["stats"][15] -= 2

                        vending_machine_break = random.randint(0,vending_machine_health)  # picks from 0- whatever the health has become, if 0 then permanent destruction
                        if vending_machine_break <= 0:
                            print("the vending machine has been permanently destroyed...")
                            vending_machine = False
                        break

                    elif scenario_chosen == 2:
                        print("you test your luck to buy a soda pop...")
                        difficulty -= 7
                        amount_stat_needed += difficulty
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
                        vending_machine_break = random.randint(0,vending_machine_health)  # picks from 0- whatever the health has become, if 0 then permanent destruction
                        if vending_machine_break <= 0:
                            print("the vending machine has been permanently destroyed...")
                            vending_machine = False
                        break


                    else:
                        print("type a number from 1-2")


                except ValueError:
                    print("type a valid number")

        else:
            print("the vending machine was broken")






    else:
        print("")

    for i in range(1,len(classes[class_area]["stats"]),2): #gets all integer values for stats
        stat_value = classes[class_area]["stats"][i] #sets random variable to whatever value of stat is
        if stat_value <= 0: #if stat is zero or lower, tells player that they lose and quits game...
            print("your",classes[class_area]["stats"][i-1],"stat is unsatisfactory, terminating player...")
            time.sleep(2)
            print("goodbye!")
            quit()

    difficulty = 0
    return difficulty #reset difficulty for future encounters


def inventory_combine(inventory): #used for combining two items into a stat boost or other item
    while True: #repeats until valid conclusion has been reached
        katana_soda = False

        print("your inventory contains: ", inventory) #shows player all items
        first_item = input("what is the first item you want to combine? or type q to leave crafting")
        if first_item in inventory: #if valid input checks for second item
            second_item = input("what is the second item you want to combine?")

            if second_item in inventory: #if valid input looks for combination recipes



                if first_item == "soda":
                    if second_item == "katana": #either combination works and disregards many bugs
                        katana_soda = True
                elif first_item == "katana":
                    if second_item == "soda":
                        katana_soda = True

                elif katana_soda:
                    print("you sharpened your skills but got liquid all over yourself... you gain 1 strength but gain 1 smell but lose a soda")
                    inventory.remove("soda")
                    classes[class_area]["stats"][1] += 1
                    classes[class_area]["stats"][9] += 1

                else:
                    print("you can't combine those two items")
                break #once combination is done or failed, they return to whatever they were doing, they can return to crafting right after if they want to.

            else:
                print("you don't have that second item combination failed") #tells player what happened

        elif first_item == "q":
            break #breaks loop and returns player
        else:
            print("you dont have that") #error messages to help player understand

def quit_or_inventory(chosen_area): #function saves having to type same batch of lines when player is choosing to do anything
    if chosen_area == "q":
        encounter_decider = 0
        skill_check_encounter(encounter_decider,difficulty)
    elif chosen_area == "i":
        inventory_combine(inventory)
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
                print("type the first letter as indicated in [] to move to/do a scenario or type i to access inventory and q to quit the game")
                time.sleep(2)
                print("you lose the game if any stat (including cash) is reduced to zero or lower")
            else:
                print("type a number from 1-3")
        except ValueError:
            print("not a valid input")


    print("Some guy that insulted your reddit account turned out to be the ceo of reddit... Steve Huffman ")
    print("your goal is to break into his large epic skyscraper and humiliate him in the most gratifying way you can imagine.")
    print("but first, you must pick your angry redditor")

    while player_choosing == True: #player selects class they play
        for i in range(0, len(classes)):
            print(classes[i]["name"], "=", i+1 )#accesses names from dictionary and prints from the range of 0-3
        try:
           class_type = int(input("type the adjacent number of the class you want to play from 1-4"))
           if 4 >= class_type >=1: #checks if within boundry limits of 4 characters
               class_area = class_type - 1 #starts from 0 for computer checking within the dictionary in the function
               print(classes[class_area]["name"])
               for i in range(0, len(classes[class_area]["stats"]),2):  # this loop shows all player stats so they can decide which is best to counter the scenario
                   print(classes[class_area]["stats"][i], " = ", classes[class_area]["stats"][i + 1])

               end_loop = input("is that your selected class type? y or n")
               while True:
                   if end_loop == "y":
                       class_type = classes[class_area]
                       player_choosing = False
                       break
                   elif end_loop == "n":
                       print("choose again")
                       break
                   else:
                       print("invalid input try again")
                       break
           else: #standard error and retrys loop
               print("type a number from 1-4")
        except ValueError: #if player didn't type an integer
            print("invalid input")


    while True:
        while phase_one == True: #start here but player could go to many different points of the game, all phases start out false and certain ones will be unlocked based on specific scenario
            chosen_area = input("you stand at the front gates of the large corporate building, you notice a [v]ending machine,the [f]ront gates, and a [m]ouldy piece of cheese on the ground. ")

            quit_or_inventory(chosen_area)

            if chosen_area == "v":
                encounter_decider = 3
                skill_check_encounter(encounter_decider,difficulty)

            elif chosen_area == "f":
                while True:
                    chosen_area = input("you are at the front of the gate, to your [l]eft there are some redditors guarding a box, to the [r]ight there is an entrance guarded by a redditor")
                    quit_or_inventory(chosen_area)
                    if chosen_area == "l":
                        encounter_decider = 2
                        print("these redditors are TUFF AND STRONG!!!, that box must be OVERPOWERED!!!")
                        difficulty = 4
                        skill_check_encounter(encounter_decider,difficulty)
                        if success == "y":

                            while True:
                                chosen_area = input("the other redditor was scared off by your power, you open the brilliant diamond case, now you must choose an item, [g]renade, [s]ack of cash, [r]andom stat boost ")
                                quit_or_inventory(chosen_area)
                                if chosen_area == "g": #take grenade
                                    print("you obtain a grenade, be careful or you will straight up die... ")
                                    inventory.append("grenade")
                                    break
                                elif chosen_area == "s": #take sack of cash
                                    one_time_random = random.randint(6,8)
                                    print("there was: ",one_time_random, "cash in the sack, so now you get that")
                                    classes[class_area]["stats"][15] += one_time_random
                                    break
                                elif chosen_area == "r":
                                    one_time_random = random.randint(0,len(list_for_gaining_stats))
                                    print("you increased your: ",classes[class_area]["stats"][one_time_random],"by one")
                                    classes[class_area]["stats"][one_time_random] += 1
                                    break
                                else:
                                    print("you do nothing and stare at the box")
                            phase_one = False
                            phase_two = True
                            print("you enter the front gates valiantly")  #straigth to phase two
                        else:
                            print("the other redditor saw your weakness and wants to beat you up too. He is slightly weaker")
                            difficulty = 3
                            skill_check_encounter(encounter_decider,difficulty)
                            if success == "y":
                                print("you leave battered and bruised")
                            else:
                                print("your beating made national headlines, you are coaxed in shame and leave, -1 to all stats")
                                for i in range(0,len(list_for_gaining_stats)):
                                    classes[class_area]["stats"][list_for_gaining_stats[i]] -= 1
                                encounter_decider = 0
                                skill_check_encounter(encounter_decider,difficulty) #checks if a stat went below 0
                    break # breaks phase one loop :D :D :D :D :D :D

            elif chosen_area == "m": # mouldy cheese path for phase 1
                print("you pick up the mouldy cheese and place it in your inventory, you seem to be a little stinkier then before...")
                classes[class_area]["stats"][9] += 1
                while phase_one == True:
                    chosen_area = input("as you stuff the cheese in you pocket you notice an entrance by the right side door, but a fat guard is blocking your path, [s]neak, [c]onfront")

                    quit_or_inventory(chosen_area)

                    if chosen_area == "s": #this isn't a multi-scenario stat chooser so it's not in the main skill check function
                        print("you try to sneak past the guard, hoping your stench doesn't attract him...")
                        amount_stat_needed = random.randint(1,20)

                        print("required stink is less than: ", amount_stat_needed)
                        time.sleep(2)
                        if amount_stat_needed > classes[class_area]["stats"][7]:
                            print("you successfully evade the guard and enter the building")
                            phase_one = False
                            phase_three = False
                        else:
                            print("you hadn't showered in the past year apparently so the guard noticed you...")
                            encounter_decider = 2
                            skill_check_encounter(encounter_decider,difficulty)
                            if success == "y":
                                print("you enter the side of the building, but you are full of shame...")
                                phase_one = False
                                phase_three = True
                            else:
                                while True:
                                    chosen_area = input("even the redditor takes pity on you, you can choose his [b]ody pillow  or authentic [j]apanese katana to take with you... ")
                                    if chosen_area == "i":
                                        inventory_combine(inventory)
                                    elif chosen_area == "q":
                                        encounter_decider = 0
                                        skill_check_encounter(encounter_decider,difficulty)
                                    elif chosen_area == "b":
                                        print("you gain a body pillow and enter the building with shame, you lose street cred")
                                        classes[class_area]["stats"][13] -= 1
                                        inventory.append("body pillow")
                                        break

                                    elif chosen_area == "j":
                                        print("you gain a katana and enter the building with shame, you lose street cred")
                                        classes[class_area]["stats"][13] -= 1
                                        inventory.append("katana")
                                        break
                                    else:
                                        print("you stand there and wiggle your toes")

                                    phase_three = True
                                    phase_one = False
                    elif chosen_area == "c":
                        encounter_decider = 2
                        success = ""
                        skill_check_encounter(encounter_decider,difficulty)
                        print(success)
                        if success == "y":
                            print("you have entered the building, the outside now does not exist")
                        else:
                            print("you failed confronting the redditor, you still enter the right side of the building but must now wear the badge of shame permanently")
                            inventory.append("badge of shame")
                        phase_one = False
                        phase_three = True
                    else:
                        print("you stand around and wait for something to happen...")
                        time.sleep(3)
                        print("to your surprise nothing did.")
                        time.sleep(2)

        while phase_two == True:
            asdfasdf = input("")

        while phase_three == True:

            input("z")


























