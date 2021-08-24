def summa(a, b):
    return float(a) + float(b)


def difference(a, b):
    return float(a) - float(b)


def product(a, b):
    return float(a) * float(b)


def division(a, b):
    return float(a) / float(b)


def division_int(a, b):
    return float(a) // float(b)


def division_rem(a, b):
    return float(a) % float(b)


def degree(a, b):
    return float(a) ** float(b)


def operations(result):
    result_list.append(result)
    print(result)


def retry():
    ans = input().lower()
    if ans == 'да':
        c, a_sign, d = input('Введите исправленную строку').split()
        conditions(c, a_sign, d)


def conditions(a, sign, b):
    try:
        if sign == '+':
            res = summa(a, b)
            operations(res)
        if sign == '-':
            res = difference(a, b)
            operations(res)
        if sign == '*':
            res = product(a, b)
            operations(res)
        if sign == '/':
            res = division(a, b)
            operations(res)
        if sign == '//':
            res = division_int(a, b)
            operations(res)
        if sign == '%':
            res = division_rem(a, b)
            operations(res)
        if sign == '**':
            res = degree(a, b)
            operations(res)
    except ZeroDivisionError:
        print('Обнаружено деление на ноль!', a, sign, b, 'Хотите исправить?', end=' ')
        retry()
    except OverflowError:
        print('Результат невозможно отобразить: слишком большой размер.', a, sign, b, 'Хотите исправить?', end=' ')
        retry()
    except ValueError:
        print('Невозможно сконвертировать данные в число', a, sign, b, 'Хотите исправить?', end=' ')
        retry()


result_list = []
with open('calc.txt', 'r') as calc:
    for i_line in calc:
        a, sign, b = i_line.split()
        conditions(a, sign, b)

print('\nСумма результатов:', sum(result_list))
