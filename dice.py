import random
import sys

def diceroll():
 min = 1
 max = 6

 roll_again = "yes"

 while roll_again == "yes" or roll_again == "y":
    print ("Rolling the dices...")
    print ("The values are....")
    print (random.randint(min, max))
    print (random.randint(min, max))
    bktodice = input("Roll Again? [y/n]")
    if bktodice == "y":
     diceroll()
    if bktodice == "n":
     sys.exit()

    
diceroll()
