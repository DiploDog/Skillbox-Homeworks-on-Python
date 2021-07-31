violator_songs = [
    ['World in My Eyes', 4.86],
    ['Sweetest Perfection', 4.43],
    ['Personal Jesus', 4.56],
    ['Halo', 4.9],
    ['Waiting for the Night', 6.07],
    ['Enjoy the Silence', 4.20],
    ['Policy of Truth', 4.76],
    ['Blue Dress', 4.29],
    ['Clean', 5.83]
]

song_duration = 0
song_quant = int(input('Сколько песен выбрать? '))
for i_song in range(song_quant):
    print('Название', i_song + 1, 'песни:', end=' ')
    song = input()
    for title in range(len(violator_songs)):
        if violator_songs[title][0] == song:
            song_duration += violator_songs[title][1]


print('Общее время звучания песен:', round(song_duration, 2), 'минут')
