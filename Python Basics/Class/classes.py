
class C:

    def __init__(self, v):
        self.x = v

    def __getitem__(self, item):
        return self.x[item]

    def __setitem__(self, key, value):
        self.x[key] = value

    def __len__(self):
        return len(self.x)

    def __add__(self, other):
        return C([self[i] + other[i] for i in range(len(self))])

    def __mul__(self, other):
        while len(self.x) < max(len(self), len(other)):
            self.x += [0]
        while len(other.x) < max(len(self), len(other)):
            other.x += [0]
        return sum([self.x[i] * other.x[i] for i in range(len(self))])

    def __repr__(self):
        s = '('
        for i in self:
            s += ' ' + str(i) + ' '
        return s + ')'

    def __pow__(self, power, modulo=None):
        return C([i ** power for i in self])


a = C([1, 2])
b = C([3, 4])

print(a)
print(b)

print(a * b)

