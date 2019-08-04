
class Class:

    def __init__(self, x):
        self.x = x

    def __getitem__(self, item):
        return self.x[item]


    def get_x(self):
        return self.x


a = Class([0., 1.])

print(a[0])
