wordlist = ["one", "two", "three"]
text = "one two"


for i, j in zip(wordlist, map(lambda x: x in text.split(), wordlist)):
    print(i, '\t', j)
