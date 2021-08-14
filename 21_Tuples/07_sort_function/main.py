def sort_tuple(a_tuple):
    a_list = [
        elem
        for elem in a_tuple
        if type(elem) == int
    ]
    if len(a_list) != len(a_tuple):
        return a_tuple
    else:
        return tuple(sorted(a_list))


some_tuple1 = (6, 5, 3, 8, 2, 7, 4, 2)
print(sort_tuple(some_tuple1))
some_tuple2 = (6, 5, 3, 8, 2, 7.2, 4, 2)
print(sort_tuple(some_tuple2))
