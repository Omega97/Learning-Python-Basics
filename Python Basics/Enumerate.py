# It allows to loop over something and have an automatic counter

v = [10 * i for i in range(5)]

for counter, value in enumerate(v):
    print(counter, value)


print(type(enumerate(v)))
