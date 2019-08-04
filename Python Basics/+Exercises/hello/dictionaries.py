
dict = {'math':'first',
        'physics':'second',
        'science':'third',
        'other':'fourth'}

print(dict['math'])

del dict['other']

dict['other'] = 'other'

print(len(dict))
print(dict.get('math'))
print(dict.keys())
print(dict.values())

