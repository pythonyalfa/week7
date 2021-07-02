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
class die:
    def __init__(self, n):
        self.__n = n

    def get_sides(self, n):
        return n
    def roll_die(self, n):
        landOn = int(random.randint(n))
        return landOn
    def roll_multiple(self, n):
        for i in n:
            n.append(i)
            multiplerolls = list(i)
            return multiplerolls


def main():

    n = eval(input("Enter the sides on the dies: "))
    die1 = die(n)
    print(die1.get_sides(n))
    print(die1.roll_die(n))
    print(die1.roll_multiple(n))

main()