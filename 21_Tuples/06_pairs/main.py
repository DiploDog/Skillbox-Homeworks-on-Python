import random

origin_list = [random.randint(0, 100) for _ in range(10)]
print('Оригинальный список:', origin_list)
new_list_1 = [(origin_list[i - 1], origin_list[i]) for i in range(1, len(origin_list), 2)]
print('Новый список (1):', new_list_1)
new_list_2 = [*map(tuple, zip(origin_list[::2], origin_list[1::2]))]
print('Новый список (2)', new_list_2)