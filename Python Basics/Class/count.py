""" count the number of the instances of a class """


class C:

    count = 0

    def __init__(self):
        C.count += 1


a = C()
b = C()

print(C.count)
