
def digit_sum(n):
    sum_digits = 0
    while n > 0:
        sum_digits += n % 10
        n //= 10

    return sum_digits


def digit_count(n):
    count = 0
    while n > 0:
        n //= 10
        count += 1

    return count


positive_num = int(input('Введите целое положительное число: '))
sum_of_digits = digit_sum(positive_num)
count_of_digits = digit_count(positive_num)

print('Сумма цифр:', sum_of_digits)
print('Количество цифр в числе:', count_of_digits)
print('Разность суммы и количества цифр:', sum_of_digits - count_of_digits)
