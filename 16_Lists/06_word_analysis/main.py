word = input('Введите слово: ')
unic_count = 0
for letter_1 in list(word):
    count = 0
    for letter_2 in list(word):
        if letter_2 == letter_1:
            count += 1
    if count == 1:
        unic_count += 1

print('\nКоличество уникальных букв:', unic_count)