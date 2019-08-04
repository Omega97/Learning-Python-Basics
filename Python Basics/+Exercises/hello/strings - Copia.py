
class MyClass:
    """ My class """
    def __init__(self, real, imaginary):
        self.r = real
        self.i = imaginary

    k = 314

    def f(self, s1, s2):
        return s1 + s2


print(MyClass.__doc__)


class Dog:

    kind = 'canine'         # class variable shared by all instances

    def __init__(self, name):
        self.name = name    # instance variable unique to each instance
        self.tricks = []    # creates a new empty list for each dog

    def add_trick(self, trick):
        self.tricks.append(trick)


d = Dog('Fido')
e = Dog('Buddy')
