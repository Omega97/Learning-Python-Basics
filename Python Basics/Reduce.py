"""
:returns f( ... f(f(a1, a2), a3) ... )
"""
from functools import reduce


v = [i for i in range(10)]

def f(x, y):
    return x + y


print(reduce(f, v))
