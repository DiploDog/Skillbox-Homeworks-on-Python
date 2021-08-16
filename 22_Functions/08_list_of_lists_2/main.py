nice_list = [1, 2, [3, 4], [[5, 6, 7], [8, 9, 10]],
             [[11, 12, 13], [14, 15], [16, 17, 18]]]


def nicer_list(a_list):
    new_list = []
    for i in a_list:
        if isinstance(i, list):
            new_list.extend(nicer_list(i))
        if isinstance(i, int):
            new_list.append(i)

    return new_list


print(nicer_list(nice_list))
