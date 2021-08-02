alphabet = ['а', 'б', 'в', 'г', 'д', 'е', 'ё',
            'ж', 'з', 'и', 'й', 'к', 'л', 'м',
            'н', 'о', 'п', 'р', 'с', 'т', 'у',
            'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ',
            'ы', 'ь', 'э', 'ю', 'я']

msg = list(input('Введите сообщение: '))
shift = int(input('Введите сдвиг: '))
cypher_list = [alphabet[(alphabet.index(msg_ltr) + shift) % (len(alphabet))]
               if msg_ltr in alphabet else ' ' for msg_ltr in msg]

print('Зашифрованное сообщение:', end=' ')
for letter in cypher_list:
    print(letter, end='')