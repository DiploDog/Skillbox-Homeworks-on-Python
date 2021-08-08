def shift_between(str_1, str_2):
    if len(str_1) == len(str_2):
        str_2 *= 2
        shift = str_2.find(str_1)
        if shift != -1:
            return '\nПервая строка получается из второй ' \
                   'со сдвигом {}'.format(shift)
        else:
            return '\nПервую строку нельзя получить из второй ' \
                   'с помощью циклического сдвига.'


string_1 = input('Первая строка: ')
string_2 = input('Вторая строка: ')
print(shift_between(string_1, string_2))
