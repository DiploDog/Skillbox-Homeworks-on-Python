from collections.abc import Iterable


class Squares:
    def __init__(self, num: int) -> None:
        self.num = num
        self.__seq = 0

    def __iter__(self) -> Iterable[int]:
        return self

    def __next__(self) -> int:
        if self.__seq == self.num:
            raise StopIteration
        else:
            self.__seq += 1
            return self.__seq ** 2


num = 5


def squares(n: int) -> Iterable[int]:
    for k in range(1, n + 1):
        yield k ** 2


print()

seq = Squares(num)
for i in seq:
    print(i)

print()


for j in squares(num):
    print(j)

print()
squares_gen = (x ** 2 for x in range(1, num + 1))
for i_sq in squares_gen:
    print(i_sq)
