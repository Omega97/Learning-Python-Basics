from main import title


@title
def reverse_array():
    """ reverse array """
    v = [i for i in range(5)]
    w = v[::-1]
    print(v)
    print(w)


@title
def swap_objects():
    """ swap objects """
    a, b = 1, 2
    b, a = a, b
    print(a, b)


@title
def sort_list_by_another_list():
    """ sort list by another list """
    v = ["two", "three", "one"]
    w = [2, 3, 1]
    v = [i for _, i in sorted(zip(w, v))]
    print(v)


@title
def double_indices_iteration():
    """ double indices iteration """
    v = [[j * 10 + i for i in range(1, 3)] for j in range(1, 4)]
    for i, j in v:
        print(i, j)


@title
def zip_example():
    """ zip example """
    v1 = [i for i in range(5)]
    v2 = [i*10 for i in range(5)]
    v3 = [i*100 for i in range(5)]
    for i in zip(v1, v2, v3):
        print(i)
    print()
    for i, j, k in zip(v1, v2, v3):
        print(i, j, k)


@title
def enumerate_list():
    """ enumerate list """
    v = ['a', 'b', 'c']
    for i, a in enumerate(v, start=1):
        print(i, a)


@title
def partial_unpack():
    # use _ for unused values
    a, _ = (1, 2)
    print(a)
    # use *var to group all the rest
    a, b, *c = (1, 2, 3, 4, 5)
    print(a, b, c)
    # use *_ to ignore all the rest
    a, b, *_ = (1, 2, 3, 4, 5)
    print(a, b)
    # use *var to group all up to the last value
    a, b, *c, d = (1, 2, 3, 4, 5)
    print(a, b, c, d)


if __name__ == '__main__':
    reverse_array()
    swap_objects()
    sort_list_by_another_list()
    double_indices_iteration()
    zip_example()
    enumerate_list()
    partial_unpack()
