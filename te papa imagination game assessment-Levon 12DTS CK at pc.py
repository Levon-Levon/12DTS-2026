






#--------------------------library imports------------------
import time
import random







#-----------------------------variables-------------------------
every_item_in_game = ["body pillow", "holy cheese", "grenade", "special key", "goop","cheese","disgusting pillow","hat of shame","soda","hat of triumph","katana"]
inventory = ["body pillow","holy cheese"]
cashier_store = ["body pillow","grenade","special key"]
endgame_shop = ["holy cheese","hat of triumph","nuke"]

endings = ["meaninglessness ending","failure ending","loser ending"] #loser ending is if you have digusting pillow and hat of shame
completed_endings = ["meaninglessness ending","failure ending","loser ending"]


vending_machine_health = 20
vending_machine = True
difficulty = 0
cashier = "alive"
phase_one_cheese = "there"
phase_two_cheese = "virgin"
player_choosing = True
chosen_area = ""
door_open = False
phase_one = True
phase_two = False
phase_three = False
phase_four = False
phase_five = False
phase_four_boss = True
phase_three_reward = True

ending_one = False
ending_two = False
success = str

list_for_gaining_stats = [1,3,5,7,9,11,13,15] #probably not efficient but helps when wanting to decrease or increase a certain stat, especially when randomizing
list_of_phases = [phase_one,phase_two,phase_three,phase_four,phase_five]
classes = [
    {"name":"bronie","stats":["strength",8,"charisma",5,"intelligence",9,"vigor",55,"smell",12,"luck",11,"street cred",2,"cash",14]}, # has all necesseray values for player
    {"name":"csgo try-hard","stats":["strength",6,"charisma",6,"intelligence",8,"vigor",65,"smell",10,"luck",6,"street cred",10,"cash",6]},
    {"name":"prime shivam","stats":["strength",12,"charisma",10,"intelligence",6,"vigor",85,"smell",6,"luck",4,"street cred",6,"cash",10]},
    {"name":"mr. E","stats":["strength",3,"charisma",12,"intelligence",11,"vigor",50,"smell",5,"luck",10,"street cred",12,"cash",21]},


]
ENCOUNTER_MESSAGES = ["", #messages correspond to each scenario, first message is blank for when checking if a stat has gone below zero or not
                      "do you want to quit the game? type 1 if you do, type 2 to keep playing.",
                      "you encounter a redditor, type 1 to punch his groin, type 2 to flex reddit karma, type 3 to flex reddit gold",
                      "you are at a vending machine, type 1 to kick machine, type 2 to purchase soda pop for $5",
                      "you encounter a gilded agent, type 1 to outsmart, 2 to strike, or 3 to charm",
                      "DO YOU WANT TO TEST YOUR SKILLS? (1), TEST YOUR FATE? (2), OR BLEED FOR PROSPERITY? (3)",
                      "you encounter Mr. Slime. type 1 to steal goop, type 2 to use item, type 3 to brace for impact and consume, (or type 4 to run like a wimp)",
                      "do you want to play memory test (1), reaction time battle (2)",
                      "YOU CANNOT RUN FROM ME YOU BASTARD... 1 to STRIKE 2 to cry, 3 to outwit, 4 to face punishment, 5 to use item. "]

#--------------------------functions-----------------------------

def ending_display(chosen_area):#function for storing ending messages when referred to around multiple parts of the game "chosen_area" parameter is for less clutter (like glb var)

    if chosen_area == "1": #if first ending was typed
        if "meaninglessness ending" in completed_endings: #if the player has the correct ending
            print("meaninglessness ending:")
            print("the ceo of reddit has finally been defeated...")
            time.sleep(4)
            print("millions go homeless... but your karma is now in the billions") #------------ending messages
            time.sleep(4)
            print("maybe you thought you would feel something... but you are filled with nothing but emptiness...")
            time.sleep(4)
            print("you sit upon the top floor of reddit incorporated, feeling unsatisfied and miserable...")
            time.sleep(4)
        else:
            print("meaninglessness ending requirement: fulfill your most thirsty desire") #win against the final boss regularly
    elif chosen_area == "2": #if second ending was typed
        if "failure ending" in completed_endings: #if player has the second ending
            print("failure ending:")
            print("amongst your best efforts, you were not able to defeat Steve Huffman")
            time.sleep(4)
            print("he hooks your brain up to some sort of machine, and you become a reddit slave for the rest of your life")
            time.sleep(4)
            print("part of you wonders what would have happened if you won, if you would have felt anything more than you do right now.")
            time.sleep(4)
            print("oh well, who really cares. Enjoy your time karma farming!!!")
            time.sleep(4)
        else:
            print("failure ending requirement: fail in the face of great mightiness") #lose to the final boss regularly
    elif chosen_area == "3":
        if "loser ending" in completed_endings:
            print("loser ending:")
            print("your stench is so overwhelming that Steve Huffman jumps out of the window of the skyscraper and is taken to anywhere but this room... ")
            time.sleep(6)
            print("you also notice that nobody else is in the building... YOU HAVE IT ALL TO YOURSELFF!!!")
            time.sleep(4)
            print("you host a parade with your body pillows, causing so much sweat and oil to leak that the earth forever becomes contaminated... (your parents couldn't be more proud)")
            time.sleep(7)
        else: #have disgusting pillow and hat of shame in your inventory when wntering the final boss fight
            print("loser ending requirement: disgust even the ceo of reddit with items that should be scorched to ash due to their rancidness and inducement of shame")

    else:
        print("that is not an ending") #if player types non-included ending number
def skill_check_encounter(encounter_decider,difficulty):#parameters encounter decider is for which scenario they do, difficulty is influenced by how they got there.
    global inventory
    global vending_machine_health # i might not need to global since these only exist within function?
    global vending_machine
    global success
    empty_list_for_shenanigans = []
    mr_slime = 3
    every_item_in_game = ["body pillow", "holy cheese", "grenade", "special key", "disgusting pillow","hat of shame"]

    print(ENCOUNTER_MESSAGES[encounter_decider]) #saves typing multiple prints for each encounter by recieveing message from list
    amount_stat_needed = random.randint(0,20+difficulty)  # rolls an imaginary D20 and if your stat is higher, then you beat encounter.
    for i in range(0, len(classes[class_area]["stats"]), 2):  # this loop shows all player stats so they can decide which is best to counter the scenario
        print(classes[class_area]["stats"][i], " = ", classes[class_area]["stats"][i + 1]) #gets first element of  stats list in player dictionary, then visually shows it equal to the next element

    if encounter_decider == 0:
        print()

    if encounter_decider == 1: #the quitting scenario, always available
       while True: #repeats specific scenario until valid outcome has been reached
           try:
                chosen_area = int(input("")) #each scenario will have multiple outcomes so loop and try and except is neccecery for the multiple outcomes
                quit_or_inventory(chosen_area)
                if chosen_area == 1: #if valid inputs the 1 and 2 do their correct corresponding actions
                    print("goodbye!")
                    quit()
                elif chosen_area == 2:
                    print("you have chosen to keep playing")
                    break
                else:
                    print("not a number from 1-2") #checks for valid input
           except ValueError:
               print("not a valid input") #checks for valid input

    elif encounter_decider == 2: #corresponding from list
        while True:
            try:
                chosen_area = int(input("choose which scenario to counter"))
                quit_or_inventory(chosen_area)

                if chosen_area == 1:#-------------------------------------------------------------------redditor scenario------------------------------------------------
                    print("you try to punch the redditor") #prints your attempted action for added clarity
                     #based on assumed "difficulty" of encounter required stats will be decreased for ease
                    print("required strength is: ", amount_stat_needed)  #shows player required stat before ending encounter
                    time.sleep(2)
                    if classes[class_area]["stats"][1] >= amount_stat_needed: #if stat is equal to or greater required then player is rewarded
                        print("you successfully punch the redditor, you gain +1 strength")
                        classes[class_area]["stats"][1] += 1
                        success = "y" #extra global output variable "success" which could potentially be used for deciding ventures for the player
                    else:
                        print("your fist bounced off his stomach and hit your face, you lose 1 strength") #if lower than player is punished
                        classes[class_area]["stats"][1] -= 1
                        success = ""
                    break

                elif chosen_area == 2:

                    print("required street cred is: ", amount_stat_needed)
                    if classes[class_area]["stats"][13] >= amount_stat_needed:
                        print("your reddit karma obliviates the redditor, you gain +1 street cred") #set success to y
                        success = "y"
                    else:
                        print("your karma is lower than his (you should post more memes bro), you lose 1 street cred")
                        classes[class_area]["stats"][13] -= 1
                        success = ""
                    break
                elif chosen_area == 3:

                    print("required luck is: ", amount_stat_needed)
                    if classes[class_area]["stats"][11] >= amount_stat_needed:
                        print("your golden soul blesses him, you gain +1 luck and he gives you 1 dollar")
                        success = "y"
                        classes[class_area]["stats"][11] += 1
                        classes[class_area]["stats"][15] += 1
                    else:
                        print("his gold overwhelms you, you lose 1 dollar for each subreddit this guy moderates (9)")
                        classes[class_area]["stats"][15] -= 9
                        success = ""
                    break

                else:
                    print("type a number from 1-3")

            except ValueError:
                print("not a number try again")




    elif encounter_decider == 3: #----------------------------------------------------------------------vending machine scenario----------------------------------
        if vending_machine == True: #if vending machine hasn't been broken by previous actions
            while True:
                try:
                    chosen_area = int(input("choose which scenario to counter")) #choosing scenario
                    quit_or_inventory(chosen_area)
                    if chosen_area == 1:
                        vending_machine_health -= 2
                        print("you kick the vending machine...")
                        print("required strength is: ", amount_stat_needed)
                        time.sleep(1)
                        if classes[class_area]["stats"][1] >= amount_stat_needed:
                            print("you successfully extract a can of soda, the vending machine looks a bit damaged though...")
                            vending_machine_health -= 2
                            inventory.append("soda")
                            success = "y"
                            break
                        else:
                            print("your foot hurts and the vending machine is now damaged and angry >:(, you lose 2 dollars and 1 strength")
                            vending_machine_health -= 1
                            classes[class_area]["stats"][1] -= 1
                            classes[class_area]["stats"][15] -= 2
                            success = ""
                            break

                        vending_machine_break = random.randint(0,vending_machine_health)  # picks from 0- whatever the health has become, if 0 then permanent destruction
                        if vending_machine_break <= 0:
                            print("the vending machine has been permanently destroyed...")
                            vending_machine = False
                            break


                    elif chosen_area == 2:
                        print("you test your luck to buy a soda pop...")
                        amount_stat_needed -=7
                        print("required luck is: ",amount_stat_needed)
                        time.sleep(1)
                        if classes[class_area]["stats"][11] >= amount_stat_needed:
                            print("you successfully buy a soda pop, you lose 5 dollars though...")
                            inventory.append("soda")
                            classes[class_area]["stats"][15] -= 5
                            success = "y"
                        else:
                            print("soda got stuck when falling, you bash your head in anger and lose intelligence on top of your money (vending machine gets damaged too)")
                            vending_machine_health -= 1
                            classes[class_area]["stats"][5] -=1
                            classes[class_area]["stats"][15] -= 5
                            success = ""
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


    elif encounter_decider == 4:#-------------------------------------------------------------gilded agent------------------------------------
        while True:
            try:
                chosen_area = int(input("choose which scenario to counter"))
                quit_or_inventory(chosen_area)
                if chosen_area == 1:
                    print("you attempt to outsmart the gilded agent")
                    print("required intelligence is: ", amount_stat_needed)
                    if classes[class_area]["stats"][5] >= amount_stat_needed:
                        print("you beat him in a chess game, he is shocked and humiliated, you gain 2 intelligence and 5 cash ")
                        classes[class_area]["stats"][5] += 1
                        classes[class_area]["stats"][15] += 5
                        success = "y"
                    else:
                        print("he beats you in a game of chess, your brain becomes mushed... -3 intelligence")
                        classes[class_area]["stats"][5] -= 3
                        success = ""
                    break
                elif chosen_area == 2:
                    print("you try to strike him as hard as you can")
                    print("required strength is: ", amount_stat_needed)
                    if classes[class_area]["stats"][1] >= amount_stat_needed:
                        print("you successfully take him down, your fists feel as if they are on fire +2 strength +5 cash")
                        classes[class_area]["stats"][1] += 2
                        success = "y"
                    else:
                        print("his might bests you, you lose all but 1 of your cash as you are knocked out as well as -1 every other stat")
                        for i in range(0, len(list_for_gaining_stats)):
                            classes[class_area]["stats"][list_for_gaining_stats[i]] -= 1
                        classes[class_area]["stats"][15] = 1
                        success = ""
                    break
                elif chosen_area == 3:
                    print("you attempt to flirt with the guy...")
                    print("required charisma is: ", amount_stat_needed)
                    if classes[class_area]["stats"][3] >= amount_stat_needed:
                        print("you rizz him up, you gain 1 charisma and double your cash")
                        classes[class_area]["stats"][5] += 1
                        classes[class_area]["stats"][15] *= 2

                        success = "y"

                    else:
                        print("he gets weirded out and knocks you out... -5 vigor, -1 charisma")
                        classes[class_area]["stats"][3] -= 1
                        classes[class_area]["stats"][7] -= 5
                        success = ""
                    break
                else:
                    print("not 1-3 do it again")

            except ValueError:
                print("that's not a scenario...")

    elif encounter_decider == 5: #-------------------------------------------------------------tarot merchant-------------------------------------------------------
        chosen_area = int(input("choose which scenario to counter"))
        quit_or_inventory(chosen_area)
        if chosen_area == 1:

            print("you fight a 3AA#2%DF&## type redditor... his toughness has been greatly randomised...")
            difficulty = random.randint(-20,40)
            encounter_decider = 2
            skill_check_encounter(encounter_decider,difficulty)
            if success == "y":
                print("YOU DID VERY GOOD SIR HAVE A CHEESE SNACK (you get cheese)")
                inventory.append("cheese")
            else:
                print("YOU WEAK DUMB BOY I BANISH YOU FROM THIS LAND (you get teleported outside of the building)")
                success = "teleport"




        elif chosen_area == 2:
            amount_stat_needed = random.randint(-30,50)
            print("required luck is: ", amount_stat_needed)
            if classes[class_area]["stats"][11] >= amount_stat_needed:
                one_time_random = random.choice(every_item_in_game)
                print("WOAHHHHHHHHHHHHHHH THATS AMAAZZZINGGGGGGGGGGGG... (you get a ", one_time_random, ")")
                inventory.append(one_time_random)
            else:
                print("you disgust me... (1 of your stats has been drained to 1)")
                one_time_random = random.choice(list_for_gaining_stats)
                classes[class_area]["stats"][one_time_random] = 1
        elif chosen_area == 3:

            amount_stat_needed = random.randint(5,15)
            one_time_random = random.choice(list_for_gaining_stats)

            classes[class_area]["stats"][one_time_random] += 1
            print("you bleed for prosperity, you lose: ", amount_stat_needed,"vigor but are rewarded with +1:",classes[class_area]["stats"][one_time_random-1])

            print("you stuff goop in your side pocket...")
            inventory.append("goop")


    elif encounter_decider == 6:#------------------------------------------Mr Slime encounter------------------------
        while mr_slime > 0: #if mr slime is alive (his value is drained after successful encounters)
            is_dead()
            chosen_area = int(input("choose which scenario to counter"))
            quit_or_inventory(chosen_area) #i need to add this everywhere
            if chosen_area == 1:
                print("you attempt to steal mr slimes goop... ")  # prints your attempted action for added clarity
                print("required strength is:",amount_stat_needed)
                if amount_stat_needed <= classes[class_area]["stats"][1]:
                    print("your hand penetrates his goopy outer layer... but did you take a poisionious piece of slime?")
                    amount_stat_needed =random.randint(0,20+difficulty)
                    print("required luck is:",amount_stat_needed)
                    if amount_stat_needed <= classes[class_area]["stats"][11]:
                        print("you steal a bit of his goop (you gain goop), mr slime has been weakened severely...")
                        inventory.append("goop")
                        mr_slime -= 1
                    else:
                        print("you are poisioned from his goop... you lose 6 vigor") #second losing scenario within first choice
                        classes[class_area]["stats"][7] -= 6
                else:
                    print("your hand gets stuck in his goopy flesh... it hrts now :(... (-1 strength, -3 vigor)") #first losing scenario
                    classes[class_area]["stats"][1] -=1
                    classes[class_area]["stats"][7] -= 1

            elif chosen_area == 2:
                print(inventory)
                chosen_area = input("choose an item to use against him...")
                if chosen_area in inventory:   #if item exists then it goes through all usable items, used for more specific error messages
                    if chosen_area == "grenade":
                        print("you attempt to use a grenade")
                        amount_stat_needed = random.randint(0, 10 + difficulty)
                        print("required luck is:" ,amount_stat_needed)
                        if amount_stat_needed <= classes[class_area]["stats"][11]:
                            inventory.remove("grenade")
                            print("you blow up a huge chunk of mr slime... but his goop poisons you (-1 to three random stats)")
                            for i in range(0,2):
                                one_time_random = random.choice(list_for_gaining_stats)
                                print("you lose 1:", classes[class_area]["stats"][one_time_random])
                                classes[class_area]["stats"][one_time_random] -= 1

                        else:
                            print("the grenade blows up in your face... you lose 15 vigor")
                            inventory.remove("grenade")
                            classes[class_area]["stats"][7] -= 15
                    else:
                        print("that item cannot be used") #if item exists but not relevant
                else:
                    print("you don't have that item")#if item doesn't exist or player doesn't have it
            elif chosen_area == 3:
                print("you brace for impact and try to consume the positive effects of the goop")
                amount_stat_needed -= classes[class_area]["stats"][5] #decreases punishment of health based on intelligence
                if amount_stat_needed <= 0:
                    amount_stat_needed = 1
                print("you will lose: ",amount_stat_needed," vigor, your intelligence saved you:",classes[class_area]["stats"][5],"points of vigor")
                amount_stat_needed = random.randint(0,20+difficulty) - classes[class_area]["stats"][5]  #rerolls for luck
                print("required luck needed for YUMMY piece of goop: ",amount_stat_needed)
                if amount_stat_needed <= classes[class_area]["stats"][11]:
                    while True:
                        one_time_random = random.choice(list_for_gaining_stats)
                        if not one_time_random == 7: #if stat is not vigor
                            print("you gained one: ", classes[class_area]["stats"][one_time_random])
                            classes[class_area]["stats"][one_time_random]
                            break #ends loop
                        else:
                            one_time_random = random.choice(list_for_gaining_stats) #this is here so nothing happens and it trys to find a stat other than vigor
                else:
                    print("you consumed a GROSS piece of goop... you lose 1 intelligence")
                    classes[class_area]["stats"][5] -= 1
            elif chosen_area == 4:
                print("required luck for running away:",amount_stat_needed)
                if amount_stat_needed <= classes[class_area]["stats"][11]:
                    print("you successfully run away, but your street cred decreases as a result of your cowardice")
                    classes[class_area]["stats"][13] -= 1
                    mr_slime = 0
                    success = "ran"
                else:
                    print("he catches you trying to run away (youre too fat lol) and you lose 3 vigor")
                    classes[class_area]["stats"][7] -= 3

        print("mr slime has been destroyed")
    elif encounter_decider == 7: #---------------------------------------------------bonus minigames encounters
        chosen_area = int(input("choose which scenario to counter"))
        if chosen_area == 1:
            mr_slime = 1
            number_to_remember = 1 #this is necesseary so that the number doesn't reset each time the loop is played
            while mr_slime <= 5:
                success = "y" #success is defaulted to "y" and only reverts once player loses but stays if they don't.
                one_time_random_one = random.randint(5,20)
                one_time_random_two = random.randint(9,11) #picking the two randomised values
                number_to_remember *= one_time_random_one * one_time_random_two #has three disposable variables to make more randomness

                print(number_to_remember)
                print("REMEMBER THESE NUMBERS!!!!!!")
                time.sleep(3)
                for i in range(0,10000): #this isn't able to hide numbers permanantly but enough to slow player down from checking
                    print("")
                while True:
                    try:
                        start_time = time.time() #starts a timer for checking player input speed

                        chosen_area = int(input("what numbers were they??? (TYPE THIS QUICKLY!!!)")) #player has to type numbers
                        end_time = time.time() #another timer for end comparison
                        elapsed_time = end_time - start_time #calculates time
                        if elapsed_time < 5: #if they were fast enough to type
                            if chosen_area == number_to_remember:
                                print("correct") #if they guessed correct
                                mr_slime += 1 #one step closer to breaking loop if correct
                            else:
                                print("WRONGGGGGGGGGGGG") #if they guessed wrong
                                mr_slime = 6
                                success = ""
                        else: #if they were too slow
                            print("too slow you failed")
                            mr_slime = 6
                            success = ""
                        break
                    except ValueError: #appropriate value error message :)
                        print("what the hell is that????")


            if success == "y":
                print("you have successfully completed the intelligence game, you get +3 intelligence")
            else:
                print("get a better brain loser lol (-4 intelligence)")
        elif chosen_area == 2: #---------------------------------------------------reaction time test game---------------------------------
            print("once you see (NOW!!! (random_key)) press [random_key]. if you are too slow you will lose some health... defeat mr_slime jr to win...")#explanation of rules
            time.sleep(7)

            slime_jr_health = 3 #sets temporary values to their standard amount that it should be.
            player_health = 3
            while True:
                list_of_random_keys = ["q","t","p","m","n","v"] #set of random keys so that player can't spam the same input
                start_time = 0
                end_time = 0 #resets timer values
                time_stop = "" #resets  variables each time
                print(player_health)
                print(slime_jr_health)
                time_wait = random.randint(2,6) #random amount of time per game
                time.sleep(time_wait)
                start_time = time.time() #starts timer once countdown ends
                one_time_random = random.choice(list_of_random_keys)
                while True:
                    print("NOW!!!",one_time_random)
                    time_stop = input("") #prints what you have to type and this loop checks if correct input was pressed
                    if time_stop == one_time_random:
                        break #breaks loop and checks time if correct input is pressed, otherwise keeps going.
                    else:
                        print("WRONG INPUT DUDE!!!") #player feedback
                end_time = time.time()
                elapsed_time = end_time - start_time #calculates the time taken.
                print("you took:",elapsed_time,"seconds.")
                if elapsed_time <= 1.45: #if within the required time limit then opposition loses -1 to its variable
                    print("GOOD JOB!!! slime jr loses a health...")
                    slime_jr_health -= 1
                else:
                    print("sorry you were to slow you lose some minigame health")
                    player_health -= 1
                if slime_jr_health == 0  or player_health == 0:
                    break
            if slime_jr_health == 0: #once broken out of loo
                print("good job for defeating mr slime jr you get +2 street cred and +2 charisma for your fast finger aura!!!")
                classes[class_area]["stats"][13] += 2
                classes[class_area]["stats"][3] += 2
                success = "y"
            else:
                print("you lose 5 street cred for you NEGATIVE AURA!!!")
                classes[class_area]["stats"][13] -= 5
                success = ""

        else:
            print("BLARGHHH")

    elif encounter_decider == 8:#-------------------------------Steve Huffman (final boss) encounter----------------------------------------------------
        steve_huffman = 5
        while steve_huffman > 0:
            chosen_area = int(input("choose which scenario to counter"))
            quit_or_inventory(chosen_area)


            if chosen_area == 1:#---------------------------------------------strike path------------------------
                print("you dare try to strike me??? (you lose 1 strength)")
                classes[class_area]["stats"][1] -= 1
                amount_stat_needed = random.randint(10,35+difficulty)
                print("required strength is:",amount_stat_needed)
                if classes[class_area]["stats"][1] > amount_stat_needed:
                    print("OUCHHHHHH HOW DARE YOU STRIKE ME!!! (Steve Huffman has been enraged, he slaps you for -2 vigor)")
                    difficulty +=3
                    classes[class_area]["stats"][2] -= 3
                    amount_stat_needed = random.randint(10,25+difficulty)
                    print("Steve Huffman tries to counter attack...")
                    print("required intelligence is:",amount_stat_needed)
                    if classes[class_area]["stats"][7] > amount_stat_needed:
                        print("ahsdfuagsdfvifuasliougb")

                else:
                    print("HAHAHAHA PATHETIC (-1 strength -5 vigor)")
                    classes[class_area]["stats"][1] -= 1
                    classes[class_area]["stats"][7] -= 5




    is_dead()
    difficulty = 0
    return difficulty #reset difficulty for future encounters





def is_dead():
    for i in range(1,len(classes[class_area]["stats"]),2): #gets all integer values for stats
        stat_value = classes[class_area]["stats"][i] #sets random variable to whatever value of stat is
        if stat_value <= 0: #if stat is zero or lower, tells player that they lose and quits game...
            print("your",classes[class_area]["stats"][i-1],"stat is unsatisfactory, terminating player...")
            time.sleep(2)
            print("goodbye!")
            quit()


def inventory_combine(inventory): #used for combining two items into a stat boost or other item
    while True: #repeats until valid conclusion has been reached

        print("your inventory contains: ", inventory) #shows player all items
        first_item = input("what is the first item you want to combine? or type q to leave crafting")
        if first_item in inventory: #if valid input checks for second item
            second_item = input("what is the second item you want to combine?")
            if second_item in inventory: #if valid input looks for combination recipes


                if first_item == "soda" and second_item == "katana" or first_item == "katana" and second_item == "soda":      #------soda katana recipe------
                    print("you sharpened your skills but got liquid all over yourself... you gain 1 strength but gain 1 smell and lose a soda")
                    inventory.remove("soda")
                    classes[class_area]["stats"][1] += 1
                    classes[class_area]["stats"][9] += 1

                elif first_item  == "katana" and second_item == "grenade" or first_item == "grenade" and second_item == "katana": # -------grenade katana recipe---------
                    print("the grenade blows up and you die instantly... game over.")
                    quit()
                elif first_item  == "holy cheese" and second_item == "body pillow" or first_item == "body pillow" and second_item == "holy cheese": #---body pillow holy cheese recipe----
                    print("two heavenly objects have been combined... the gods bless you... (+3 to every stat)")
                    inventory.remove("body pillow")
                    inventory.remove("holy cheese")
                    inventory.append("disgusting pillow")
                    for i in range(0,len(list_for_gaining_stats)):
                        classes[class_area]["stats"][list_for_gaining_stats[i]] += 3
                elif first_item  == "holy cheese" and second_item == "katana" or first_item == "katana" and second_item == "holy cheese": #----holy cheese and body pillow recipe--------
                    print("you have done a holy act... for your strength will now be handsomely rewarded... (+7)")
                    inventory.remove("holy cheese")
                    classes[class_area]["stats"][1] += 7
                elif first_item == "goop" and second_item == "goop": #-----------------------------------goop recipe--------------------------------
                    if inventory.count("goop") >=2:
                        print("you combined gunk to create a tasty snack, ( +5 vigor)")
                        classes[class_area]["stats"][7] += 5
                    else:
                        print("not enough goop")

                else:
                    print("you can't combine those two items")
                 #once combination is done or failed, they return to whatever they were doing, they can return to crafting right after if they want to.

            else:
                print("you don't have that second item combination failed") #tells player what happened


        elif first_item == "q":
            break #breaks loop and returns player to whatever they were doing
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
            player_option = int(input("type 1 to start game, type 2 to exit, type 3 for how to play, type 4 to see endings"))
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
            elif player_option == 4: #ending viewer option in main menu
                for i in range(0,len(endings)): #prints amounts of endings
                    endings_check = endings[i] #sets other variable to check for variable in another list by setting the value to the according ending in the list
                    if endings_check in completed_endings: #adds status after ending to improve player readability. checks if endings are in list of completed ones
                        status = "completed" #if have gotten ending then it will show as completed
                    else:
                        status = "incomplete" #if haven't gotten ending then will show incomplete
                    print("ending", i + 1, "=", endings[i]) #prints according messages displaying the ending name and the status later
                    print("status: ", status)
                    print("")
                try:
                    chosen_area = input("type according numbers of each ending to display the ending... only works if you have completed the ending at least once (type q to promptly leave)")
                    if chosen_area == "q": #this is more clean then showing the "thats not an ending" message in the function
                        print("")
                    else:
                        ending_display(chosen_area) #if player didn't want to quit then refers to function
                except ValueError:
                    print("what the heck is that????")


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
                                    one_time_random = random.choice(list_for_gaining_stats)
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
                                print("you enter the building feeling battered and bruised... yet successful")
                                phase_one = False
                                phase_two = True
                            else:
                                print("your beating made national headlines, you are coaxed in shame and leave, -1 to all stats")
                                for i in range(0,len(list_for_gaining_stats)):
                                    classes[class_area]["stats"][list_for_gaining_stats[i]] -= 1
                                encounter_decider = 0
                                skill_check_encounter(encounter_decider,difficulty) #checks if a stat went below 0
                    break # breaks phase one loop :D :D :D :D :D :D

            elif chosen_area == "m": # mouldy cheese path for phase 1
                if phase_one_cheese == "there":
                    print("you pick up the mouldy cheese and place it in your inventory, you seem to be a little stinkier then before...")
                    classes[class_area]["stats"][9] += 1
                    phase_one_cheese = False
                else:
                    print("there is no cheese here.... maybe it was just your imagination???")
                while phase_one == True:
                    chosen_area = input("as you stuff the 'cheese' in your pocket you notice an entrance by the right side door, but a fat guard is blocking your path, [s]neak, [c]onfront")

                    quit_or_inventory(chosen_area)

                    if chosen_area == "s": #this isn't a multi-scenario stat chooser so it's not in the main skill check function
                        print("you try to sneak past the guard, hoping your stench doesn't attract him...")
                        amount_stat_needed = random.randint(1,20)

                        print("required stink is less than: ", amount_stat_needed)
                        time.sleep(2)
                        if amount_stat_needed > classes[class_area]["stats"][9]:
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
                            inventory.append("hat of shame")
                        phase_one = False
                        phase_three = True
                    else:
                        print("you stand around and wait for something to happen...")
                        time.sleep(3)
                        print("to your surprise nothing did.")
                        time.sleep(2)

        while phase_two == True:
            chosen_area = input("you see a [d]oor with a special lock, a fat looking [c]ashier, and a [f]resh looking piece of cheese")
            quit_or_inventory(chosen_area)
            if chosen_area == "d": #door path
                if door_open == False:
                    chosen_area = input("you approach the locked door, you can try to [o]pen door, [d]etonate door or [l]eave")
                    if chosen_area == "o":
                        if "special key" in inventory:
                            inventory.remove("special key")
                            door_open = True
                            print("the special key perfectly slots into the lock, and you enter the door with great expectations...")
                            phase_two = False
                            phase_five = True
                        else:
                            print("you do not have the correct item to open this door")
                    elif chosen_area == "d":
                        if "grenade" in inventory:
                            door_open = True
                            inventory.remove("grenade")
                            print("you throw a grenade at the door, blowing it up as well as yourself, -1 to every stat")
                            time.sleep(1)
                            print("you have also alerted a high profile guard...")
                            for i in range(0, len(list_for_gaining_stats)):
                                classes[class_area]["stats"][list_for_gaining_stats[i]] -= 1
                            encounter_decider = 2
                            difficulty = 5
                            skill_check_encounter(encounter_decider,difficulty)
                            if success == "y":
                                print("you have achieved victory, you may enter through...")
                            else:
                                print("you have been bested by the guard...")
                                time.sleep(2)
                                print("he throws you out the building")
                                phase_two = False
                                phase_one = True



                        else:
                            print("you do not have the correct item to open this door")

                    elif chosen_area == "l":
                        print("you leave the locked door")
                    else:
                        print("you stand there awkwardly for a few seconds then leave...")
                        time.sleep(3)
                else:
                    print("you enter through the previously entered door...")
                    phase_two = False
                    phase_five = True


            elif chosen_area == "c":
                if cashier == "alive":
                    chosen_area = input("WELCOME TO MY CHUNKO STORE!!!! I HAVE [a]NIME PILLOWS FOR $9, [g]RENADES FOR $11 AND A [s]UPER DUPER SPECIAL KEY FOR $30!!! or [c]HALLENGE ME FOR MY STORE!!!")
                    quit_or_inventory(chosen_area)
                    if chosen_area == "a":
                        if "body_pillow" in cashier_store:
                            print("you buy a body pillow from the man... you sick freak")
                            inventory.append("body pillow")
                            cashier_store.remove("body pillow")
                            classes[class_area]["stats"][15] -= 9
                            print("you now have:",classes[class_area]["stats"][15]," dollars left")
                            encounter_decider = 0
                            skill_check_encounter(encounter_decider, difficulty)
                        else:
                            print("he doesn't have that anymore")
                    elif chosen_area == "g":
                        if "grenade" in cashier_store:
                            print("you buy a grenade from the man...")
                            inventory.append("grenade")
                            cashier_store.remove("grenade")
                            classes[class_area]["stats"][15] -= 11
                            print("you now have:",classes[class_area]["stats"][15]," dollars left")
                            encounter_decider = 0
                            skill_check_encounter(encounter_decider, difficulty)
                    elif chosen_area == "s":
                        if "special key" in cashier_store:
                            print("you buy a special from the man...")
                            cashier_store.remove("special key")
                            inventory.append("special key")
                            classes[class_area]["stats"][15] -= 30
                            print("you now have:", classes[class_area]["stats"][15], " dollars left")
                            encounter_decider = 0
                            skill_check_encounter(encounter_decider, difficulty)
                    elif chosen_area == "c":
                        encounter_decider = 4
                        difficulty = 8
                        print("the cashier rips his clothes off and reveals a hulking body of muscle... this fight is going to be tough...")
                        skill_check_encounter(encounter_decider, difficulty)
                        if success == "y":
                            print("the cashier is gone forever... but you have free reign over everything in the store (you take everything)")
                            cashier = "defeated"
                            for i in range(0,len(cashier_store)):
                                inventory.append(cashier_store[i])
                                cashier_store.remove(cashier_store[i])
                        else:
                            print("LOSER LOSER YOU'RE A HUGE LOSERRRRRRR. NEVER COME TO MY STORE AGAIN HEHEHEHEHEHEHEHEHE")
                            cashier = "you lost"
                    else:
                        print("ummmmm...... i don't have that")

                elif cashier == "you lost":
                        print("I DONT SELL TO LOSERS HAHAHAHAHAHAHA")

                else:
                    print("he's dead you monster...")


            elif chosen_area == "f":
                if phase_two_cheese == "virgin":
                    print("you decide to touch the cheese... little did you know it was a TRAP!!!! a powerful gilded agent approaches you")

                    encounter_decider = 4
                    difficulty = 5
                    skill_check_encounter(encounter_decider, difficulty)
                    if success == "y":
                        while True:
                            while phase_two_cheese == "virgin":
                                chosen_area = input("you defeat the agent and steal a special key hidden in his underpants and 3 dollars :$) do you want to [e]at cheese or [t]ake it?")
                                classes[class_area]["stats"][15] += 3
                                inventory.append("special key")
                                quit_or_inventory(chosen_area)
                                if chosen_area == "e":
                                    print("you gain +1 to every stat and feel refreshed")
                                    phase_two_cheese = "eaten"
                                    for i in range((0,7),2):
                                        classes[class_area]["stats"][list_for_gaining_stats[i]] += 1

                                elif chosen_area == "t":
                                    print("you gained: holy cheese")
                                    phase_two_cheese = "taken"
                                    inventory.append("holy cheese")

                                else:
                                    print("you have to do something with the cheese...")

                            chosen_area = input("do you want to the [r]eturn to the previous area or [c]ontinue down the hall?")
                            quit_or_inventory(chosen_area)
                            if chosen_area == "r":
                                print("you went back...")
                                break
                            elif chosen_area == "c":
                                print("you continue onwards...")
                                phase_two = False
                                phase_four = True
                                break

                            else:
                                print("invalid input")

                    else:
                        print("your humiliating defeat distracts the gilded agent... you are able to continue past him further into the building")
                        phase_two = False
                        phase_four = True

                else:
                    print("there was no cheese on the ground... maybe it was just your imagination???")
                    time.sleep(2)
                    print("before you have time to reflect, you are approached by an armed guard")
                    encounter_decider = 2
                    difficulty = 2
                    skill_check_encounter(encounter_decider, difficulty)
                    if success == "y":
                        print("you continue through the building earning 1 dollar for the victory")
                        classes[class_area]["stats"][15] += 1
                        phase_two = False
                        phase_four = True
                    else:
                        print("you are promptly kicked out for such loser behaviour")


        while phase_three == True:
            chosen_area = input("you enter the side of the building... a [t]arot merchant lays ahead, a [v]ending machine is beside you, a [w]all of computers sits behind a glass pane  ,[r]eturn.")
            quit_or_inventory(chosen_area)
            if chosen_area == "v":
                difficulty = 0
                encounter_decider = 3
                skill_check_encounter(encounter_decider, difficulty)


            elif chosen_area == "t":
                encounter_decider = 5
                skill_check_encounter(encounter_decider, difficulty)
                if success == "teleport":
                    phase_three = False
                    phase_one = True
            elif chosen_area == "w":
                chosen_area = input(" you enter an area with large rows of [c]ubicles and [p]eople sitting at their desks, somebody left their [l]aptop open.")
                quit_or_inventory(chosen_area)
                if chosen_area == "c": #--------------------------cubicle with large reddit attack---------------------
                    print("you scan the cubicles... and see a hidden pathway leading to an interesting looking doorway, but as you approach you are swarmed by gilded agents and redditors...  ")
                    encounter_decider = 2
                    difficulty = 6
                    skill_check_encounter(encounter_decider, difficulty)
                    if success == "y":
                        print("a redditor was scared off... but a powerful gilded agent approaches you...")
                        encounter_decider = 4
                        difficulty = 14
                        skill_check_encounter(encounter_decider, difficulty)
                        if success == "y":
                            if phase_three_reward == True:
                                while True:
                                    chosen_area = input("you successfully scared off every opponent in your path... a mystical pony lets you have: [g]ilded cash bag, [h]at of triumph, or [c]ompany nuke$$$$$$ ")
                                    quit_or_inventory(chosen_area)
                                    if chosen_area == "g":
                                        one_time_random = random.randint(30,44)
                                        print("the cash bag contained:",one_time_random,"dollars (you get that money now :D)")
                                        classes[class_area]["stats"][15] += one_time_random

                                    elif chosen_area == "h":
                                        print("you feel heroic and powerful... (+3 to every stat) (you also get a hat of triumph)")
                                        for i in range(0, len(list_for_gaining_stats)):
                                            classes[class_area]["stats"][list_for_gaining_stats[i]] += 3
                                        inventory.append("hat of triumph")

                                    elif chosen_area == "c":
                                        print("you get a company nuke...")
                                        inventory.append("company nuke")
                                    else:
                                        print("mehmehmehmehmemh")

                                    phase_three_reward = False
                                    break
                            else:
                                if "random dead guy in horse costume" in inventory:
                                    print("there was no mystical pony... but you see a remnant of its goop... (you get goop and a....... wait what??????)")
                                    print("you get a random dead guy in horse costume")
                                    inventory.append("goop")
                                    inventory.append("random dead guy in horse costume")
                                else:
                                    print("you get some goop, but if feels like something else used to be here....")
                                    inventory.append("goop")
                            phase_three = False
                            phase_four = True
                        else:
                            print("you are humiliated and tired... but some guy kicks you in the butt which goes through time and space (you are teleported to a random location)")
                            one_time_random = random.randint(0,len(list_of_phases))
                            phase_three_reward = False
                            list_of_phases[one_time_random] = True

                    else:
                        print("you are ashamed... (-1 street cred")
                        classes[class_area]["stats"][13] -= 1

                elif chosen_area == "p": #this sections is purposely done in order as each item holds a different level of significance...
                    print("you alert a large army of redditors to your location...")
                    if "hat of shame" in inventory:
                        print("they take notice of your short comings and grant you a mystical holy cheese (you get holy cheese)")
                        inventory.append("holy cheese")
                        print("you move further into the building")
                        phase_four = False #skipped to end area from this point based on "shameful" item
                        phase_five = True
                    elif "katana" in inventory:
                        print("it seems you want a challenge boy... let's see if you're worthy of that Japanese sword...")
                        encounter_decider = 2
                        difficulty = 10 #high difficulty because of late game area...
                        print("(a HUGE swarm of angry redditors is upon you... may god save your soul... ")
                        limit = 4
                        for i in range(0,limit): #the fights continue until the player has successfully defeated 5 redditors. A variable is used here to ensure this works.
                            print("another redditor attacks")
                            skill_check_encounter(encounter_decider, difficulty)
                            if success == "y":
                                print("the redditors take notice of your strength...") #gets rid of one if  victory is returned through "success" variable
                                limit -=1
                            else:
                                print("the redditors take notice of your weakness...")  #no change happens but player is given feedback
                    elif "body pillow" in inventory:
                        while True:
                            chosen_area = input("that is a pretty kawaii body pillow bro... I'll give you like $15 bucks for it... [y]es, [n]o")#more options for this section

                            if chosen_area == "y":
                                print("COOL THANKS BROOOOO THIS CHARACTER IS SO CUTEEEEEEEE!!!!!!")  #appropriate changes are made
                                classes[class_area]["stats"][15] += 15
                                inventory.remove("body pillow")
                                phase_four = False
                                phase_five = True
                                break
                            elif chosen_area == "n":
                                print("heh heh heh... you dare deny me of my WAIFUS!!!!")
                                encounter_decider = 4
                                difficulty = 8
                                skill_check_encounter(encounter_decider, difficulty)
                                if success == "y":
                                    print("alright bro...... ARGHGHHH YOU KEEP THE PILLOW HERE'S ALL MY MONEY IM SORRY (+30 dollars + 1 to all stats)")
                                    classes[class_area]["stats"][15] += 30
                                    for i in range(0, len(list_for_gaining_stats)):
                                        classes[class_area]["stats"][list_for_gaining_stats[i]] += 1
                                    phase_four = False
                                    phase_five = True
                                    break
                                else:
                                    print("YOU SUCKKKKKKKKKKKKKLK (you are kicked out of the building)")
                                    phase_four = False
                                    phase_one = True
                                    break

                    else: #if player has none of the above three items in their inventory
                        print("all the redditors laugh at you as you walk by because you seem so goddamn boring... -1 to all stats and you lose all your street cred...")
                        for i in range(0, len(list_for_gaining_stats)):
                            classes[class_area]["stats"][list_for_gaining_stats[i]] -= 1
                        classes[class_area]["stats"][15] = 1
                        phase_four = False
                        phase_five = True
                elif chosen_area == "l": #special minigame
                    print("you play a funny game on this guys computer...")
                    encounter_decider = 7
                    skill_check_encounter(encounter_decider, difficulty)
                    if success == "y":
                        print("your hacking skills go noticed by the redditors around you... they give you +4 karma points and +1 atheist brainpower (+4 street cred, +1 intelligence)")
                        classes[class_area]["stats"][13] += 4
                        classes[class_area]["stats"][15] += 1
                        phase_four = False
                        phase_five = True
                    else:
                        print("the redditors notice your failure and you are kicked out of there cubicles (you lose 5 vigor)")
                        phase_four = False
                        phase_one = True


            elif chosen_area == "r":
                print("you leave the building")
                phase_one = True
                phase_three = False
            else:
                print("you stand around doing nothing...")
                time.sleep(3)
                print("shockingly nothing happens.")
                time.sleep(2)





        while phase_four == True:
            chosen_area = input("you come across a [v]ending machine, a large [b]oss stands in the way")
            if chosen_area == "v":
                encounter_decider = 3
                skill_check_encounter(encounter_decider,difficulty)
            elif chosen_area == "b":
                if phase_four_boss == True:
                    encounter_decider = 6
                    skill_check_encounter(encounter_decider, difficulty)
                    if success == "ran":
                        print("you pee your pants and leave the building entirely...")
                        phase_one = True
                        phase_four = False
                        phase_four_boss = False
                    else:
                        print("the great mr slime has been defeated... you are able to progress through further into the building")
                        phase_four = False
                        phase_five = True
                else:
                    print("as you pass through you notice a glob of goop on the ground... you take it. (you gained goop)")
                    inventory.append("goop")
                    phase_four = False
                    phase_five = True


        while phase_five == True:
            chosen_area = input("you have entered the final zone... do you want to (f)inal battle, (v)ending machine, (t)arot merchant, (e)ndgame shop or (c)owardice teleport? ")
            quit_or_inventory(chosen_area)
            if chosen_area == "f":
                encounter_decider = 8
                skill_check_encounter(encounter_decider,difficulty)
                if success == "y":
                    ending_one = True
                else:
                    ending_two = True
                phase_five = False


            elif chosen_area == "v":
                encounter_decider = 3
                difficulty = 7
                skill_check_encounter(encounter_decider,difficulty)
            elif chosen_area == "t":
                encounter_decider = 5
                difficulty = 6
                skill_check_encounter(encounter_decider, difficulty)
            elif chosen_area == "e":
                chosen_area = input("hello there... welcome to my humble abode... I sell [h]oly cheese for $20, [d]ome hat of triumph for $25, and [n]uke for $99, you can [f]ight me too i guess... [r]eturn")
                quit_or_inventory(chosen_area)
                if chosen_area == "h":
                    chosen_area = "holy cheese"
                    if chosen_area in endgame_shop:
                        endgame_shop.remove(chosen_area)
                        classes[class_area]["stats"][15] -= 20
                        print("enjoy your delicious cheeseeee :)")
                        inventory.append("holy cheese")
                        encounter_decider = 0
                        skill_check_encounter(encounter_decider,difficulty)
                    else:
                        print("i don't have that anymore...")
                elif chosen_area == "d":
                    chosen_area = "hat of triumph"
                    if chosen_area in endgame_shop:
                        endgame_shop.remove(chosen_area)
                        classes[class_area]["stats"][15] -= 25
                        print("you seem worthy of such a cap")
                        inventory.append("hat of triumph")
                        encounter_decider = 0
                        skill_check_encounter(encounter_decider,difficulty)
                    else:
                        print("i don't have that anymore...")
                elif chosen_area == "n":
                    chosen_area = "nuke"
                    if chosen_area in endgame_shop:
                        endgame_shop.remove(chosen_area)
                        classes[class_area]["stats"][15] -= 25
                        print("...")
                        inventory.append("nuke")
                        encounter_decider = 0
                        skill_check_encounter(encounter_decider, difficulty)
                    else:
                        print("i don't have that anymore...")
                elif chosen_area == "f":
                    print("you seem to underestimate my strength...")
                    encounter_decider = "i dont know yet but not 8"
                    skill_check_encounter(encounter_decider, difficulty)

        if ending_one == True:
            print("you have gotten ending 1: meaninglessness ending")
            chosen_area = "1"
            completed_endings.append("meaninglessness ending")
            ending_display(chosen_area)
            ending_one = False
        if ending_two == True:
            print("you have gotten ending 2: failure ending")
            chosen_area = "2"
            completed_endings.append("failure ending")
            ending_display(chosen_area)
            ending_two = False