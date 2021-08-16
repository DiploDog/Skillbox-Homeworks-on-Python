def calculating_math_func(data):
    if data not in factorial_dict:
        result = 1
        for index in range(1, data + 1):
            result *= index
        factorial_dict[data] = result
    else:
        result = factorial_dict.get(data)

    return (result / data ** 3) ** 10


factorial_dict = dict()
while True:
    print(calculating_math_func(int(input('Введите число: '))))
