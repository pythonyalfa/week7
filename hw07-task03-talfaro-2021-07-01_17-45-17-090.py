# Task 03 Create a rectangle class with the following methods:
#    - A constructor that takes a length and width as parameters
#- A get_rect method that will return the length and width of the rectangle
#- A get_area method that will return the area of the rectangle
#- A is_square method that will return true if the rectangle is square
# - Overload equivalence to compare the length and width of two rectangles and return
#true if they are equal

#Class usage Example output of script
#abrect = Rectangle(10,10)
#cdrect = Rectangle(10,10)
#shrect = Rectangle(10,15)
#shrect.getrect()                           10, 15
#abrect.get_area()                          100
#cdrect.is_square()                         True
#shrect == abrect                           False
#abrect == cdrect                           True


class Rectangle():
    def __init__(self, length, width):
        self.__length = length
        self.__width = width

    def get_rect(self):
        return self.__length, self.__width

    def get_area(self):
        return self.__width * self.__length

    def is_square(self):
        if self.__length == self.__width:
            return True
        if self.__length != self.__width:
            return False


def main():
    abrect = Rectangle(10, 10)
    cdrect = Rectangle(10, 10)
    shrect = Rectangle(10, 15)
    print(shrect.get_rect())
    print(abrect.get_area())
    print(cdrect.is_square())
    print(shrect == abrect)
    print(shrect.get_rect())
    print(cdrect.get_rect())
    print(abrect == cdrect)

main()