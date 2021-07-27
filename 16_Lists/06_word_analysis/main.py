word = input('Введите слово: ')
count = 0
unic_letters = []
cas_letters = []
for letter in list(word):
    if letter not in unic_letters and letter not in cas_letters:
        unic_letters.append(letter)
        count += 1
    elif letter in unic_letters:
        cas_letters.append(letter)
        unic_letters.remove(letter)
        count -= 1

print('\nКоличество уникальных букв:', count)
print(unic_letters)