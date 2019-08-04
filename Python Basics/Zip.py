""" glue lists together """

v = [1, 2, 3]
w = [4, 5, 6]

for i in zip(v, w):
    print(i)


for i, j in zip(v, w):
    print(i, j)
