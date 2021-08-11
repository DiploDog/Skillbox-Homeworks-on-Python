text = input('Введите текст: ').lower()

print('Оригинальный словарь частот: ')
letter_dict = dict()

for letter in text:
    if letter in letter_dict:
        letter_dict[letter] += 1
    else:
        letter_dict[letter] = 1

for i_letter in letter_dict:
    print(i_letter, ':', letter_dict[i_letter])

new_dict = dict()
print('\nИнвертированный словарь частот:')
for i in range(1, max(letter_dict.values()) + 1):
    new_list = [key for key in letter_dict.keys()
                if letter_dict.get(key) == i]
    new_dict[i] = new_list
    print(i, ':', new_dict[i])
