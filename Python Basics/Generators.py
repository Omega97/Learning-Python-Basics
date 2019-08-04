
# A generator is a function that returns an object (iterator) which we can iterate over (one value at a time)

# It is fairly simple to create a generator in Python.
# It is as easy as defining a normal function with yield statement instead of a return statement

# The difference is that, while a return statement terminates a function entirely,
# yield statement pauses the function saving all its states and later continues from there on successive calls.

from main import title


@title
def example_1():
    """ generator from a string """

    def gen(string):
        # A simple generator function
        for i in string:
            yield i

    for c in gen("hello"):
        print(c)


@title
def example_2():
    """ powers of 2 """

    def pow_2(max_=0):
        """ 2**n """
        n = 0
        while n < max_:
            yield 2 ** n
            n += 1

    for c in pow_2(5):
        print(c)


if __name__ == "__main__":

    example_1()
    example_2()
