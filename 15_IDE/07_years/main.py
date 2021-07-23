
A = int(input('Введите первый год: '))
B = int(input('Введите второй год: '))
if A > B or 10 ** 4 < A < 10 ** 5 or 10 ** 4 < B < 10 ** 5:
    print('Ошибка значения!')
else:
    print('Года от', A, 'до', B, 'с тремя одинаковыми цифрами:')
    for year in range(A, B + 1):
        first_digit = ''
        second_digit = ''
        count_by_first = 0
        count_by_second = 0
        years = str(year)
        for digit in years:
            if first_digit == '':
                first_digit += digit
                count_by_first += 1
                continue
            elif second_digit == '':
                second_digit += digit
                count_by_second += 1
                continue
            elif digit == first_digit:
                count_by_first += 1
            elif digit == second_digit:
                count_by_second += 1
        if count_by_second == 3 or count_by_first == 3:
            print(years)

