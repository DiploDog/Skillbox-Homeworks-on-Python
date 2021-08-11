def is_palindrome(string):
    """Сообщает можно ли составить палиндром из заданной строки,
        путем множественных или единичных перестановок символов"""

    letter_dict = dict()
    letter_list = [letter for letter in string]     # заполняем буквами список

    for letter in letter_list:
        if letter not in letter_dict:
            letter_dict[letter] = 1             # также заполняем словарь
        else:                                   # буквами(ключ) и их значениями
            letter_dict[letter] += 1

    am_max = 0
    count = 0

    for amount in letter_dict.values():
        if am_max % 2 + amount % 2 != 2:            # исключаем равные нечетные значения типа aaabbb
            if amount >= am_max and amount != 1:    # исключаем набор из значений == 1
                am_max = amount                     # фиксируем максимум
                count += amount

    if count > len(string) - count and count - len(set(letter_list)) != 1:
        return 'Можно сделать палиндромом'
    else:
        return 'Нельзя сделать палиндромом'


print(is_palindrome(input('Введите строку: ')))
