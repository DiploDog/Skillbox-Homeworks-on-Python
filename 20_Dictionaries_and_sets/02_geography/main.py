def is_city(ndict, city):
    for key in ndict:
        if city in ndict.get(key):
            return 'Город {} находится в стране {}.'.format(
                city, key
            )
    else:
        return 'По городу {} данных нет.'.format(city)


n_country = int(input('Количество стран: '))
country_dict = dict()

for i_country in range(n_country):
    print(i_country + 1, 'страна:', end=' ')
    country_list = input().split()
    country_dict[country_list[0]] = {country_list[i] for i in range(1, 4)}
print()

for i_city in range(3):
    print(i_city + 1, 'город:', end=' ')
    city = input()
    print(is_city(country_dict, city))
    print()
