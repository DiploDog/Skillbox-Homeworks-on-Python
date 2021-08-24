import logging

name = input('Введите Ваше имя: ')
logging.basicConfig(filename='chat.log', level=logging.INFO)
log = logging.getLogger(name)

while True:
    try:
        print('\nВыберите действите (1 - посмотреть текущий текст чата,'
              '2 - Отправить сообщение в чат):', end=' ')
        ans = int(input())
        if ans == 1:
            with open('chat.log', 'r', encoding='utf-8') as file:
                for i_line in file:
                    print(i_line)
        if ans == 2:
            msg = input('Введите сообщение: ')
            log.info(msg)
        if ans not in (1, 2):
            raise ValueError
    except ValueError:
        print('Выберите из предлагаемых функций чата (1 или 2).')
