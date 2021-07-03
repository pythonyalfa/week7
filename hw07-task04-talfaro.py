# Task 4 Write a die rolling class that contains the following methods:
#    - A constructor that accepts an integer representing the number of sides on the die.
# - A get_sides method that will return the number of sides
# - A roll method that will return a random number as a result of rolling the die
# - A roll_multiple method that takes a number of rolls and returns a list of the results

#Class usage Example output of script
#idie = Die(20)
#idie.get_sides()                        20
#idie.roll()                             14
#idie.roll_multiple(4)                   [4,16,1,9]
import random


class Die:
    def __init__(self, n):
        self.n = n

    def get_sides(self, n):
        return n

    def roll_die(self, n):

        return random.randint(1,n)


    def roll_multiple(self, n):
        x = []
        for i in range(0, n):
            x.append(self.roll_die(n))
        return x



def main():

    #n = eval(input("Enter the sides on the dies: "))
    n = 43
    idie = Die(n)
    print(idie.get_sides(n))
    print(idie.roll_die(n))
    print(idie.roll_multiple(5))

main()