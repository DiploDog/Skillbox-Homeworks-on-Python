import random


def f(x, y):
    x += random.randint(0, 10)
    y += random.randint(0, 5)
    return x / y


def f2(x, y):
    x -= random.randint(0, 10)
    y -= random.randint(0, 5)
    return y / x


line_count = 0
with open('coordinates.txt', 'r') as file:
    for line in file:
        line_count += 1
        func_num = 1
        nums_list = line.split()
        try:
            res1 = round(f(int(nums_list[0]), int(nums_list[1])), 1)
            func_num += 1
            res2 = round(f2(int(nums_list[0]), int(nums_list[1])), 1)
            number = random.randint(0, 100)
            my_list = sorted([res1, res2, number])
            with open('result.txt', 'a') as file_2:
                file_2.write('{} {} {}\n'.format(
                    my_list[0],
                    my_list[1],
                    my_list[2]
                ))
                func_num = 1

        except ZeroDivisionError:
            with open('result.txt', 'a') as file_2:
                file_2.write('Обнаружена попытка деления на ноль\n')
            print('Ошибка! Обнаружена попытка деления на ноль в '
                  '{} функции для чисел {} строки'.format(func_num, line_count))


with open('result.txt', 'a') as file_2:
    file_2.write('\n')
