import os


# write on file
def write_file(name, str_array, num):
    test_file = open(name, "wb")
    for I in range(0, num):
        test_file.write(bytes(str(str_array[I]) + "\n", "UTF-8"))
    test_file.truncate()
    test_file.close()


testFile = open("name.txt", 'r+')
text = testFile.read()
testFile.seek(0)
testFile.write(str(n) + "\n")
testFile.write(str(i) + "\n")
testFile.write("10 ^ " + str(math.log(i, 10)))
testFile.truncate()
testFile.close()


testFile = open("name.txt", "wb")   # use "ab+" to read and append
print(testFile.mode)  # file mod
print(testFile.name)
testFile.write(bytes("Hello\n", "UTF-8"))
testFile.close()


testFile = open("name.txt", "r+")
textInFile = testFile.read()
print(textInFile)
testFile.close()

os.remove("name.txt")
