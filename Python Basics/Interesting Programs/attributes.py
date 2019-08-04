
def new_attribute(object, name, default=None):
    exec('object.' + name + '=default')


class Class:

    def __init__(self):
        pass


a = Class()
new_attribute(a, 'one', default=1)
new_attribute(a, 'two', default=2)
print(vars(a))
