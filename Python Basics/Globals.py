
# all global variables (attributes)
print(globals(), '\n')

# a method that will return, as a list, every associated method or attribute
print(dir(), '\n')

# will print out the docstring that appears in a class or method


def f():
    """ Simple function """
    pass


print(f.__doc__, '\n')

# specifies the module name, and the current namespace in __name__
print(__file__, '\n')

# defines the namespace that a Python module is running in
print(__name__, '\n')

# used instead of __name__ to calculate explicit relative imports for main modules
print(__package__, '\n')
