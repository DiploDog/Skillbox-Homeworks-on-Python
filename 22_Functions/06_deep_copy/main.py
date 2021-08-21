import copy

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

    return dct


sites_dict = dict()
site_num = int(input('Сколько сайтов: '))

for _ in range(site_num):
    site_name = input('\nВведите название продукта для нового сайта: ')
    new_site = site_maker(copy.deepcopy(site), site_name)
    sites_dict[site_name] = new_site

    for key in sites_dict.keys():
        print('\nСайт для {}:'.format(key))
        print('site =', sites_dict.get(key))
