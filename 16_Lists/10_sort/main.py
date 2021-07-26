N = int(input('Введите количество чисел в списке: '))
num_list = []
for num in range(N):
    print('Введите', num + 1, 'число:', end=' ')
    number = int(input())
    num_list.append(number)
print('\nИзначальный список:', num_list)

for i in range(len(num_list)):
    for j in range(i + 1, len(num_list)):
        if num_list[i] > num_list[j]:
            num_list[i], num_list[j] = num_list[j], num_list[i]

print('\nОтсортированный список:', num_list)



