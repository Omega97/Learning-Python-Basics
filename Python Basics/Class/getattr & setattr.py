""" """
from main import title


@title
def example_1():

    class C:
        pass

    a = C()
    setattr(a, 'x', 1)
    print(vars(a))


@title
def example_2():

    class C:
        pass

    a = C()
    dic = {'x': 1, 'y': 2, 'z': 3}

    for i, v in dic.items():
        setattr(a, i, v)
    print(vars(a))

    for key in dic.keys():
        print(getattr(a, key))


@title
def example_3():

    class C:
        def __init__(self, **kwargs):
            for i in kwargs:
                setattr(self, i, kwargs[i])

    a = C(a=1, b=2)
    print(list(filter(lambda x: x[0] != '_', dir(a))))


if __name__ == '__main__':

    example_1()
    example_2()
    example_3()
