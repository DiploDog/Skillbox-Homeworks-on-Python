def list_filling(n):
    my_list = []
    for _ in range(n):
        my_list.append(int(input('Введите число: ')))

    return my_list


print('Первый список')
list_1 = list_filling(3)
print('\nВторой список')
list_2 = list_filling(7)
list_1.extend(list_2)
for i in list_1:
    while list_1.count(i) > 1:
        list_1.remove(i)

print('Новый первый список с уникальными элементами:', list_1)

#print(set(list_1))