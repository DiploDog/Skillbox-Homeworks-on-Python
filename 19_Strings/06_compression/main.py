def string_zip(string) -> str:
    tmp = list(string[:1])
    string = string[1:]
    parts = [tmp]

    for letter in string:
        if letter in tmp:
            tmp.append(letter)
        else:
            tmp = [letter]
            parts.append(tmp)

    return ''.join('{}{}'.format(part[0], len(part)) for part in parts)


my_string = input('Введите строку: ')
print('Закодированная строка:', string_zip(my_string))
