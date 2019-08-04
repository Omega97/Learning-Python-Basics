
array = ['']*4  # empty string array

list1 = ['pi', 'phi', 'tau']


print('first = ', list1[0])

list1[2] = 'gamma'
print(list1[0:2])


list2 = [1, 2, 3]

all_lists = [list1, list2]

print(all_lists[0][2])

list1.append("sigma")
print(list1)

list1.insert(2, 'alpha')
list1.remove('sigma')
print(list1)

list1.sort()
print(list1)

list1.reverse()
print(list1)

del list2[2]
print(list2)

pi_tuple = (3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7, 9, 3)
new_tuple = list(pi_tuple)
new_list = tuple(new_tuple)


print(min(list1))


class Person(object):
    """__init__() functions as the class constructor"""
    def __init__(self, name=None, job=None, quote=None):
        self.name = name
        self.job = job
        self.quote = quote
