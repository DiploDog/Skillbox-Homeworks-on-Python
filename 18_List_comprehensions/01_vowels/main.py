phrase = input('Введите текст: ')
vowels = [vowel for vowel in phrase if vowel in list('ауоиэыяюеёАУОИЭЫЯЮЕЁ')]
print('Список гласных букв:', vowels)
print('Длина списка:', len(vowels))