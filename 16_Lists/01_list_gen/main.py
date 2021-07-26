N = int(input('Введите целое положительное число: '))
odds = []
for num in range(1, N + 1):
    if num % 2 != 0:
        odds.append(num)

print(odds)