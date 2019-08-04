def near_thousand(n):
    return ((abs(1000 - n) <= 100) or (abs(2000 - n) <= 100))

a = int(input("n = "))
print(near_thousand(a))
