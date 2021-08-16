def fibonacci(n):
    if n in (1, 2):
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


print('\nЧисло:', fibonacci(int(input('Введите позицию числа Фибоначчи: '))))
