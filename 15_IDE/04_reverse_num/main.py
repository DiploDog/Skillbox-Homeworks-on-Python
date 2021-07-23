
def reverse_num(num):
    rev_num_int = ''
    for symbol in str(num):
        if symbol == '.':
            break
        else:
            rev_num_int = symbol + rev_num_int

    return rev_num_int


def reverse_fract(num):
    num_str = str(num)
    parts = num_str.split('.')
    rev_num_fract = ''
    for symbol in parts[1]:
        rev_num_fract = symbol + rev_num_fract

    return rev_num_fract


def parts_str_num(part_int, part_fract):
    new_num = float(part_int + '.' + part_fract)

    return new_num


N = float(input('Введите первое вещественное число: '))
K = float(input('Введите второе вещественное число: '))
print()

part_int_N = reverse_num(N)
part_fract_N = reverse_fract(N)
parts_str_N = parts_str_num(part_int_N, part_fract_N)

part_int_K = reverse_num(K)
part_fract_K = reverse_fract(K)
parts_str_K = parts_str_num(part_int_K, part_fract_K)

print('Первое число наоборот:', parts_str_N)
print('Второе число наоборот:', parts_str_K)
print('Сумма:', parts_str_N + parts_str_K)