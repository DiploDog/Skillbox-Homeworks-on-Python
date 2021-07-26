films = ['Крепкий орешек', 'Назад в будущее', 'Таксист',
         'Леон', 'Богемская рапсодия', 'Город грехов',
         'Мементо', 'Отступники', 'Деревня']

my_films = []
print('Чтобы перейти к списку выбранных фильмов, нажмите Enter')
while True:
    film = input('Введите название фильма: ')
    if film in films:
        my_films.append(film)
    elif film not in films and film != '':
        print('Ошибка! Такого фильма у нас нет.')
    elif film == '':
        break

print('Список выбранных фильмов:')
for i in my_films:
    print(' ' * 23, '+', i)
