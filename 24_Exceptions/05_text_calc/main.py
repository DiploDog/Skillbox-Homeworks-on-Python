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


result_list = []
with open('calc.txt', 'r') as calc:
    for i_line in calc:
        a, sign, b = i_line.split()
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
            print('Обнаружено деление на ноль!')
        except OverflowError:
            print('Результат невозможно отобразить: слишком большой размер.')
        except ValueError:
            print('Невозможно сконвертировать данные в число')

print('Сумма результатов:', sum(result_list))

