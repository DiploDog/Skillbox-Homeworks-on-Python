import os.path


def string_letters_operations(file):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    alpha_count = 0
    string_count = 0
    chars_dict = dict()
    for i_line in file:
        for char in i_line:
            if char.lower() in alphabet:
                alpha_count += 1
            if char == '\n':
                string_count += 1
            char = char.lower()
            if char not in chars_dict and char in alphabet:
                chars_dict[char] = 1
            if char in chars_dict and char in alphabet:
                chars_dict[char] += 1
    for char, value in chars_dict.items():
        if value == min(chars_dict.values()):
            return alpha_count, string_count, char, chars_dict


def how_many_words(file):
    count_words = 0
    for i_line in file:
        string_list = i_line.split()
        count_words += len(string_list) - i_line.count(' -- ')

    return count_words


file = open(os.path.abspath(os.path.join('..', '02_zen_of_python', 'zen.txt')), 'r')
chars, strings, char_min, letters_count = string_letters_operations(file)
file.seek(0)
words = how_many_words(file)
file.close()

print('Букв:', chars, 'строк:', strings, 'слов:', words,
      '\nСамая редкая буква:', char_min)
print('Словарь букв:', letters_count)

