from math import sqrt


class Vector:

    def __init__(self, x):
        self.x = x

    def __add__(self, other):
        v = []
        for i in range(max(len(self.x), len(other.x))):
            s = 0
            if i < len(self.x):
                s += self.x[i]
            if i < len(other.x):
                s += other.x[i]
            v.append(s)
        return Vector(v)

    def __sub__(self, other):
        v = []
        for i in range(max(len(self.x), len(other.x))):
            s = 0
            if i < len(self.x):
                s += self.x[i]
            if i < len(other.x):
                s -= other.x[i]
            v.append(s)
        return Vector(v)

    def __mul__(self, other):
        s = 0
        for i in range(min(len(self.x), len(other.x))):
            s += self.x[i] * other.x[i]
        return s

    def __getitem__(self, item):
        return self.x[item]

    def __lt__(self, other):
        return True if self.length() < other.length() else False

    def __gt__(self, other):
        return True if self.length() > other.length() else False

    def __le__(self, other):
        return True if self.length() <= other.length() else False

    def __ge__(self, other):
        return True if self.length() >= other.length() else False

    def __eq__(self, other):
        return True if self.x == other.x else False

    def __ne__(self, other):
        return not self == other

    def get_x(self):
        return self.x

    def length(self):
        out = 0
        for i in range(len(self.x)):
            out += self.x[i] ** 2
        return sqrt(out)

    def show(self):
        print(self.get_x())


if __name__ == "__main__":

    a = Vector([1, 2])
    b = Vector([2, 2, 1])

    c = a + b   # This is the cool part
    d = a - b

    a.show()
    b.show()
    c.show()
    d.show()

    print(a * b)    # and so is this
    print(a[0])
    print(a.length())
    print(b.length())
    print(a < b)
    print(a == b)
    print(a != b)
