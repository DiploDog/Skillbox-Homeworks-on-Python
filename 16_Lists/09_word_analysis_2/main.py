word = input('Введите слово: ')
word_in_list = list(word)
word_out_list = []
flag = True

for i_letter in range(len(word_in_list) - 1, -1, -1):
    word_out_list.append(word_in_list[i_letter])
    if word_in_list[len(word_in_list) - i_letter - 1] == word_out_list[len(word_out_list) - 1]:
        flag = True
    else:
        flag = False

if flag:
    print('\nСлово является палиндромом')
else:
    print('\nСлово не является палиндромом')
