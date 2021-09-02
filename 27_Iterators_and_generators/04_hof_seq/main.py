from typing import List
from collections.abc import Iterable


def qhoff(nums: List, user_range: int) -> Iterable[int]:
    if nums == [1, 2]:
        return
    qhoff_list = [nums[0], nums[1]]
    for _ in range(user_range + 1):
        new_num = qhoff_list[-qhoff_list[-1]] + qhoff_list[-qhoff_list[-2]]
        qhoff_list.append(new_num)
        yield qhoff_list[-1]


my_nums = [1, 1]
rng = 50
for i in qhoff(my_nums, rng):
    print(i, end=' ')