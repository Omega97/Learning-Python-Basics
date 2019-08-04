# A namespace is a mapping from names to objects, with the property that
# there is zero relation between names in different namespaces


class MyClass:

    class_var = 0

    def __init__(self, i_var):
        self.i_var = i_var


print("\nMyClass.class_var =", MyClass.class_var)


foo = MyClass(2)

print("\n\ni_var is in foo's instance namespace\n")
print(foo.__dict__)
print('i_var =', foo.i_var)


print("\n\nclass_var isn't in instance namespace...")
print("So we look in class namespace (MyClass.__dict__)\n")
print(MyClass.__dict__)
print(foo.class_var)
