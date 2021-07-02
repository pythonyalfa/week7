# Task 05
# Write a coin ﬂipping class that inherits from the die class. Bet you never thought of a coin as a
# two sided die. It would contain the following changes:
# - The constructor should not take any arguments as a coin usually only has two sides
# - A ﬂip method that uses the roll method. If the roll is 1, return "HEADS". if it is 2, return "TAILS"

#Class usage Example output of script
#nickle = Coin()
#nickle.roll()                          #1
#nickle.flip()                          #TAILS
#nickle.roll_multiple(4)                #[1, 1, 2, 1]
import array
import random


class Coin:
    def __init__(self):
        pass
    def roll(self):
        x = random.choice([True, False])
        if x == True:
            x = 1
        else:
            if x == False:
                x = 2
        return x
    def flip(self):
        x = random.choice([True, False])
        if x == True:
            x = "Heads"
        else:
            if x == False:
                x = "Tails"
        return x

    def roll_multiple(self, n):

            return n




def main():

    nickel = Coin()
    print(nickel.roll())
    print(nickel.flip())
    print(nickel.roll_multiple(4))

main()