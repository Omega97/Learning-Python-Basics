
s = "Bosa the dog"

print(s)
print("%s %s" % (s,"!"))

print(len(s))

print('\n' * 2)


print(s[0:4])
print(s[:-3])
print(s[-3:])


print('funny '+s+'!')

print('%s %c %d %.5f' % ('str','c',10,12.34))

print(s.capitalize())
print(s.find("Bosa"))
print(s.isalpha())
print(s.isalnum())
print(s.replace('dog','doggy'))
print(s.strip())

list =s.split(" ")
print(list)

