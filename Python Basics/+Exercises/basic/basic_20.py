def larger_string(s, n):
    result = ""
    for i in range(n):
        result = result + s
    return result

print(larger_string('abc', 2))
print(larger_string('.py', 3))
