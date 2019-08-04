def new_string(s):
    if len(s) >= 2 and s[:2] == "Is":
        return s
    return "Is" + s

print(new_string("Array"))
print(new_string("IsEmpty"))
