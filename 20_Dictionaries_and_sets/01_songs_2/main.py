violator_songs = {
    'World in My Eyes': 4.86,
    'Sweetest Perfection': 4.43,
    'Personal Jesus': 4.56,
    'Halo': 4.9,
    'Waiting for the Night': 6.07,
    'Enjoy the Silence': 4.20,
    'Policy of Truth': 4.76,
    'Blue Dress': 4.29,
    'Clean': 5.83
}

total_dur = 0

songs_amount = int(input('Сколько песен выбрать? '))
for i_song in range(songs_amount):
    print('Название {}-й песни:'.format(i_song + 1), end=' ')
    total_dur += violator_songs.get(input())

print('\nОбщая продолжительность звучания песен: {:.2f} минут'.format(
    total_dur
))
