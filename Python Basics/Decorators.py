"""
A decorator is a function that takes another function
and extends the behavior of the latter function
without explicitly modifying it
"""
from time import time
from main import title


@title
def example_1():
    """ example 1 """
    def a(f):
        # simple decorator
        def wrapper():
            # wrapping method
            print("pre-Whee")
            f()
            print("post-Whee")
        return wrapper

    @a
    def say_whee():
        # dummy method
        print("Whee!")

    say_whee()


@title
def example_2():
    """ example 2 """
    def a(f):
        # decorator with arguments
        def wrapper(*args, **kwargs):
            print('before')
            f(*args, **kwargs)
            print('after')

        return wrapper

    @a
    def fun(s):
        print(s)

    fun('fun')


@title
def example_3():
    """ example 3 """
    def do_twice(f):
        # repeat attributes twice
        def wrapper():
            f()
            f()
        return wrapper

    @do_twice
    def greet(name='Bosa'):
        print(f"Hello {name}")

    greet()


@title
def example_4():
    """ example 4 """
    def a(f):
        def wrapper(*args, **kwargs):
            return f(*args, **kwargs)
        return wrapper

    @a
    def fun(name):
        print("fun call")
        return f"Hi {name}"

    print(fun('Omar'))


@title
def example_5():
    """ example 5 """
    def lapse(f):
        # take the time it takes to execute a method
        def wrapper():
            t0 = time()
            f()
            print('t = %.5f s' % (time()-t0))
        return wrapper

    @lapse
    def foo():
        for _ in range(10**5):
            pass

    foo()


@title
def example_6():

    def dec(f):
        print('init dec')

        def w(*ar, **kw):
            print('w', ar, kw)
            return f(*ar, *kw)
        return w

    @dec
    def fun(*args, **kwargs):
        print('fun', args, kwargs)
        return 'output', args, kwargs

    print()
    print(fun, '\n')
    print(fun(1, k=2), '\n')


if __name__ == "__main__":
    example_1()
    example_2()
    example_3()
    example_4()
    example_5()
    example_6()
