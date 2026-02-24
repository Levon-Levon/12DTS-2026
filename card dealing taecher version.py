
import time
import random


VALUES = [1,2,3,4,5,6,7,8,9,10,11,12,13]
SUITS = ["Hearts","Clubs","Spades","Diamonds"]
deck = [[],[]]
hand = [[],[]]


def hand_draw(amount):
    for i in range(0,amount):
        value = random.randint(0,len(deck[0])-1)
        hand[0].append(deck[0][value])
        deck[0].pop(value)
        hand[1].append(deck[1][value])
        deck[1].pop(value)
    print(hand)

def ordered_cards():
    print('poo')


print("building deck")
for x in SUITS:

    for y in VALUES:
        deck[0].append(x)
        deck[1].append(y)
        print("card:",y,"of",x, "added")
        time.sleep(0.001)
    print("done!")
print("deck contents:")
for i in range(0,len(deck[0])-1):
    print("card",i,"is:",deck[0][i],deck[1][i])


print(deck)
amount = int(input('how many cards do you want to draw'))
hand_draw(amount)

