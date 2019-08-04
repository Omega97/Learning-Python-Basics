
path = 'test.txt'

# automatically closes the file
with open(path, 'w') as f:
    f.write('a')

# automatically closes the file
with open(path) as f:
    file_content = f.read()


print(file_content)
