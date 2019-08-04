def sum_thrice(x, y, z):
    s = x + y + z

    if x == y == z:
        s = s * 3
    return s

print(sum_thrice(1, 2, 3))
print(sum_thrice(3, 3, 3))
