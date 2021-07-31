N = int(input('Количество коньков: '))
pairs = []
for i in range(N):
    print('Размер', i + 1, 'пары:', end=' ')
    pair = int(input())
    pairs.append(pair)

K = int(input('\nКоличество людей: '))
persons = []
for i in range(K):
    print('Размер ноги', i + 1, 'человека:', end=' ')
    person = int(input())
    persons.append(person)

fit = 0
for guy in persons:
    for size in pairs:
        if guy <= size:
            pairs.remove(size)
            fit += 1
            break

print('\nНаибольшее количество людей, которые могут взять ролики:', fit)