# Task 02 - Create a dog breed class with a constructor that takes the following:
#   - Name
#   - Life expectancy
#   - Size
#   - Coat type (limit to long, short, curly, etc.)
#   - Coat color/pattern

#Class Usage :
# gr = Dog("Golden Retriever”, 12, "large", "medium", "gold")
# pg = Dog("Pug", 15, "small", "short","silver fawn")
# cg = Dog("Corgi", 13, "smol", "fluffy","tricolor")



class Dog():
    def __init__(self, name, life, size, coatType, coatColor):
        self.__name = name
        self.__life = life
        self.__size = size
        self.__coatType = coatType
        self.__coatColor = coatColor
    def get_name(self):
        return self.__name
    def get_life(self):
        return self.__life
    def get_size(self):
        return self.__coatType
    def get_coatColor(self):
        return self.__coatColor

def main():
    gr = Dog("Golden Retreiver", 12, "large","medium", "gold")
    pg = Dog("Pug", 15, "small", "short", "silver fawn")
    cg = Dog("Corgi", 13, "small", "fluffy", "tricolor")
    print("I have three dogs. Their breeds are,",gr.get_name(),',', pg.get_name(),',', cg.get_name())
    print("My pug is",pg.get_life(),"years old.")
main()