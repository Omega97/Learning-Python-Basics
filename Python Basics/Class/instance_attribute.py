
class MyClass(object):
    # class attribute
    class_var = 0

    def __init__(self, i_var):
        # instance attribute
        self.i_var = i_var
        MyClass.class_var += 1


foo = MyClass(2)
bar = MyClass(3)

print(foo.class_var, foo.i_var)
print(bar.class_var, bar.i_var)

# all instances of the class have access to class_var
print(MyClass.class_var)
