import random


def cut_tuple(tpl, elem):
    if tpl.count(elem) >= 2:
        nxt_elem = 1
        for i, j in enumerate(tpl):
            if i > tpl.index(elem) and j == elem:
                nxt_elem += i
                break
        return tpl[tpl.index(elem):nxt_elem]

    if tpl.count(elem) == 1:
        return tpl[tpl.index(elem):]

    else:
        return tuple()


rand_tpl = tuple(random.randint(0, 10) for _ in range(10))
print(rand_tpl)
print(cut_tuple(rand_tpl, int(input('Введите элемент: '))))
