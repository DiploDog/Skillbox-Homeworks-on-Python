def not_eq(my_list: set) -> int:
    """Проверяет на равенство последовательные
            объекты списка с конца. Возвращает следующий, неравный
                предыдущему, элемент с конца списка"""
    for k in range(1, len(my_list) + 1):
        for n in range(k, len(my_list) + 1):
            if my_list[-k] != my_list[-n]:
                break
        break

    return n


N = int(input('Количество чисел: '))
num_list = []
for _ in range(N):
    num_list.append(int(input('Число: ')))

to_add = []
for j in range(not_eq(num_list), N + 1):
    to_add.append(num_list[-j])

print('\nПоследовательность:', end=' ')
for i in num_list:
    print(i, end=' ')
print('\nНужно приписать чисел:', len(to_add))
print('Сами числа:', end=' ')
for u in to_add:
    print(u, end=' ')