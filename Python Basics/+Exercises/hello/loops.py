import random


# for

for i in range(0, 5):
    print(i, '  ', end='')
print('\n')


lista = ['A', 'B', 'C', 'D']
for j in lista:
    print(j, ' ', end='')
print('\n')


for j in [2, 4, 6, 8]:
    print(j, ' ', end='')
print('\n')


# nested for

newList = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for i in range(0, 3):
    for j in range(0, 3):
        print(newList[i][j])


# while

randomNum = random.randrange(0, 10)
while randomNum != 1:
    print(randomNum)
    randomNum = random.randrange(0, 10)
print('\n')


i = 0
while i <= 20:
    if i % 2 == 0:
        print(i)
    elif i == 9:
        break
    else:
        i += 1  # i = i+1
        continue    # jump back to while loop
    i += 1
print("\n"*2)


# prime numbers

n = 20
i = 2
while i <= n:
    j = 2
    while j*j <= i:
        if i % j == 0:
            break
        else:
            j = j + 1
    if j*j > i:
        print(i, " is prime")
    i = i + 1

print("Good bye!")
