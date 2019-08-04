
class Class:

    def __init__(self, v=None):
        self.array = v
        self.index = 0

    def __len__(self):
        return len(self.array)

    def __getitem__(self, item):
        return self.array[item]

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self):
            self.index = 0
            raise StopIteration
        else:
            i = self.index
            self.index += 1
            return self[i]


A = Class(['o' * i for i in range(1, 5)])

for i in A:
    print(i)
print()
for i in A:
    print(i)
