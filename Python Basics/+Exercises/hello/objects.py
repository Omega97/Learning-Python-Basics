

# class definition

class Animal:       # __ means private
    __name = ""
    __height = 0
    __weight = 0
    __sound = 0


    # setting up

    def __init__(self, name, height, weight, sound):   # redefined later
        self.__name = name
        self.__height = height
        self.__weight = weight
        self.__sound = sound


    # setters

    def set_name(self, name):    # "self" allows an object to refer to itself inside of a class
        self.__name = name

    def set_height(self, height):
        self.__height = height

    def set_weight(self, weight):
        self.__weight = weight

    def set_sound(self, sound):
        self.__sound = sound


    # getters

    def get_name(self):
        return self.__name

    def get_height(self):
        return self.__height

    def get_waight(self):
        return self.__weight

    def get_sound(self):
        return self.__sound

    def get_type(self):
        print("Animal")

    def to_string(self):
        return "{} is {} cm tall and {} Kg and says {}".format(self.__name,
                                                               self.__height,
                                                               self.__weight,
                                                               self.__sound)


# how it looks like

cat = Animal("Whiskers", 33, 10, "Miao")
print(cat.toString())


# new class
class Dog(Animal):
    __owner = ""

    def __init__(self, name, height, weight, sound, owner):
        self.__owner = owner
        super(Dog, self).__init(name, height, weight, sound) #super-class

        def set_owner(self, owner):
            self.__owner = owner

        def get_owner(self):
            return self.__owner

        def get_type(self):
            print("Dog")


# method overloading = perform different tasks based of different tasks
#   based of different attributes in input

    def multiple_sounds(self, how_many = None):
        if how_many is None:
            print(self.get_sound())
        else:
            print(self.get_sound() * how_many)


spot = Dog("Bosa",53,27,"Ruff", "Lofy")

print(spot.toString())



#an other class
class AnimalTesting:
    def get_type(self, animal):
            animal.get_type()


test_animals = AnimalTesting()

test_animals.get_type(cat)
test_animals.get_type(spot)

spot.multiple_sounds(4)
