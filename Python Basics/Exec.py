""" execute a string as if it was code """

s = "print(1)"
s = s + '\n' + s
exec(s)
