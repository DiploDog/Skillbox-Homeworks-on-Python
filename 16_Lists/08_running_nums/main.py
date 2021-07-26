N = int(input('Число элементов списка: '))
num_list = []
new_num_list = []
for _ in range(N):
    n = int(input('Введите число для табло: '))
    num_list.append(n)

shift = int(input('\nСдвиг: '))
if shift > N: # Костыль для (псевдо)цикличности :)
    shift %= N

for i_num in range(len(num_list)):
    if i_num + shift >= len(num_list):
        new_num_list.append(num_list[i_num])
else:
    for i_num in range(len(num_list)):
        if i_num + shift > len(num_list) - 1:
            continue
        else:
            new_num_list.append(num_list[i_num])

print('Изначальный список:', num_list)
print('Сдвинутый список:', new_num_list)

