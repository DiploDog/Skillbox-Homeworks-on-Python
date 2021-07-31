word = input('Введите слово: ')
count = 0
unic_letters = []
unique_count = 0
for char in word:
    if char not in unic_letters:
        unic_letters.append(char)
        unique_count += 1


print('\nКоличество уникальных букв:', unique_count)
print(unic_letters)