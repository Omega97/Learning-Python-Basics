

def attributes(a: str):
    """ print all attributes of an object """
    s = "for i in dir(" + a + "):" + "\n\t"
    s += "print('{:20s}'.format(i), end='')" + "\n\t"
    s += "exec('print(" + a + ".' + i + ')')"
    exec(s)


def f():
    return

class C:
    pass

attributes('C')
