N = int(input('Введите максимальное число: '))
artyom_numbers = {i for i in range(1, N + 1)}

boris_list = input('\nНужное число есть среди вот этих чисел? ').split()
boris_set = set()
while boris_list != ['Помогите!']:
    boris_list = set(boris_list)
    artyom_ans = input('Ответ Артема: ')
    if artyom_ans == 'Да':
        boris_set.update(boris_list)
    if artyom_ans == 'Нет':
        boris_set = boris_set.difference(boris_list)
    boris_list = input('\nНужное число есть среди вот этих чисел? ').split()

print('Артема мог загадать следующие числа:', end=' ')
for i in boris_set:
    print(i, end=' ')