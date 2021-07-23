
def ld(num):
    least_div = 0
    for div in range(2, num + 1):
        if num % div == 0:
            least_div = div
            break

    return least_div


num = int(input('Введите натуральное число n > 1: '))
if num < 1:
    print('Ошибка, обратите внимание на требование!')
else:
    least_divider = ld(num)
    print('Наименьший делитель, отличный от единицы, числа', num, 'равен', least_divider)