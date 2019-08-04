""" sort iterables """
from main import title


@title
def basic_string():
    """ basic string """
    s1 = 'a'
    s2 = 'a' + 'b' + 'c'
    print(s1, s2)


@title
def join_strings():
    """ join strings """
    a = [str(i) for i in range(1, 5)]
    print("  ".join(a))


@title
def string_to_list():
    """ string_to_list """
    s = '123'
    v = [i for i in s]
    print(v)


@title
def reverse_string():
    """ reverse string """
    a = "a b c d e"
    print(a[::-1])


@title
def percentage_format():
    """ percentage format """
    print('%d  %.3f  %+.3f' % (1, 1.2, 1.23))
    print('%8.2f %8.4f %8.6f' % (1, 2, 3))


@title
def format():
    """ format """
    print(' a) {:d}   b) {:s} '.format(1, 'b'))


@title
def functional_string():
    """ functional string """
    def attributes(x, n):
        return attributes"{x} " * n
    print(attributes('dog', 9))


@title
def useful():
    """ useful """
    s = 'a b c d e'
    print(s)
    s = s.replace(' ', '_')
    print(s)
    s = s.replace('_', '')
    print(s.index('a'))
    print(s.count('_'))


if __name__ == "__main__":

    basic_string()
    join_strings()
    reverse_string()
    string_to_list()
    percentage_format()
    format()
    functional_string()
    useful()
