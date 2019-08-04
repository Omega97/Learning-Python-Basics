""" map(method, iterator)
 applies the method to the iterator """


def f(x):
    return x**2


v = [1, 2, 3]

print(map(f, v))
print(list(map(f, v)))


v = [('a', 1), ('b', 2), ('c', 3)]


def g(x):
    return x[0], f(x[1])


print(list(map(g, v)))
