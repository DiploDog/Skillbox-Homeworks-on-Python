import random

N = ['I' * 1 for _ in range(int(input('Количество палок: ')))]
K = int(input('Количество бросков: '))

for i_throw in range(K):
    L_i = random.randint(1, random.randint(1, len(N)))
    R_i = random.randint(L_i, len(N))
    N[L_i - 1:R_i] = ['.' * 1 for _ in range(R_i - L_i + 1)]
    print('Бросок', str(i_throw + 1) + '. Сбиты палки с номера', L_i)
    print('по номер', R_i)
    #print('Результат:', N)

print('Результат:', end=' ')
for cond in N:
    print(cond, end='')
