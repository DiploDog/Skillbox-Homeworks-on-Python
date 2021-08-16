site = {
    'html': {
        'head': {
            'title': 'Куплю/продам {product} недорого'
        },
        'body': {
            'h2': 'У нас самая низкая цена на {product}',
            'div': 'Купить',
            'p': 'продать'
        }
    }
}


def site_maker(dct, prod):

    for sub_dct in dct.values():
        if isinstance(sub_dct, dict):
            if 'title' in sub_dct.keys():
                sub_dct['title'] = 'Куплю/продам {product} недорого'.format(product=prod)
            if 'h2' in sub_dct.keys():
                sub_dct['h2'] = 'У нас самая низкая цена на {product}'.format(product=prod)
            else:
                site_maker(sub_dct, prod)



sites_dict = dict()
site_num = int(input('Сколько сайтов: '))
for _ in range(site_num):
    site_name = input('Введите название продукта для нового сайта: ')
    if site_name not in sites_dict.keys():
        sites_dict[site_name] = site
    site_maker(sites_dict[site_name], site_name)
    print(sites_dict)

for key in sites_dict.keys():
    print('\nСайт для {}:'.format(key))
    print(sites_dict.get(key))



