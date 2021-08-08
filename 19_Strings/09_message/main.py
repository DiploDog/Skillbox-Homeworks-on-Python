def phrase_roll(phrase):
    phrase_list = list(phrase)
    new_list = []
    word = ''

    for symb in phrase_list:
        if symb.isalpha():
            word += symb
        else:
            new_list.append(word[::-1])
            new_list.append(symb)
            word = ''

    return ''.join(new_list)


msg = input('Сообщение: ')
new_msg = phrase_roll(msg)
print('\nНовое сообщение:', new_msg)
