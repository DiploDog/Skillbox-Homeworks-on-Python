def is_synonym(sm_dict, word):
    for key in sm_dict:
        if key == word:
            return 'Синоним: {}'.format(sm_dict.get(key))
        if sm_dict.get(key) == word:
            return 'Синоним: {}'.format(key)
    else:
        return 'Такого слова в словаре нет.'


pairs = int(input('Введите количество пар слов: '))

synonym_dict = dict()

for i_pair in range(pairs):
    print(i_pair + 1, 'пара:', end=' ')
    pair = input().split(' - ')
    synonym_dict[pair[0]] = pair[1]

while True:
    word = input('\nВведите слово: ').capitalize()
    print(is_synonym(synonym_dict, word))
