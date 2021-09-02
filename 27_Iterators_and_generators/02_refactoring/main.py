from collections.abc import Iterable
from typing import Any

list_1 = [2, 5, 7, 10]
list_2 = [3, 8, 4, 9]
to_find = 56


def gen() -> Iterable[Any]:
    for x in list_1:
        for y in list_2:
            result = x * y
            print(x, y, end=' ')
            yield result
            if result == to_find:
                print('Found!!!')
                return


for i in gen():
    print(i)
