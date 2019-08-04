# https://pynative.com/python-basic-exercise-for-beginners/
from omar_utils.basic.decorators import title


@title
def ex1():
    """Question 1
    Accept two int values from user and return their product.
    If the product is greater than 1000, then return their sum"""
    def f(a, b):
        return a * b if a * b <= 1000 else a + b

    print(f(5, 500))


@title
def ex2():
    """Question 2
    Given a range of numbers.
    Iterate from o^th number to the end number and print the sum of the current number and previous number"""
    def f(r, o):
        for i in range(o, len(r)-1):
            print(r[i]+r[i+1])

    f(range(10), 2)


@title
def ex3():
    """Question 3
    Accept string from the user and display only those characters which are present at an even index"""
    def f(s):
        return ''.join([s[i] for i in range(len(s)) if i % 2])

    print(f('abcdef'))


@title
def ex4():
    """Question 4
    Given a string and an int n,
    remove characters from string starting from zero up to n and return a new string"""
    def f(s, n):
        return s[n:]

    print(f('12345', 3))


if __name__ == "__main__":

    ex1()
    ex2()
    ex3()
    ex4()
