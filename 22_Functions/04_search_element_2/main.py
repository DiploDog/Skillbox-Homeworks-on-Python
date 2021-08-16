site = {
    'html': {
		'head': {
			'title': 'Мой сайт'
		},
		'body': {
			'h2': 'Здесь будет мой заголовок',
			'div': 'Тут, наверное, какой-то блок',
			'p': 'А вот здесь новый абзац'
		}
	}
}


def is_key(struct, key, deep=None):
	if key in struct:
		return struct[key]

	if deep is not None:
		deep -= 1
		if deep == 1:
			sub_key = None
			return sub_key

	for sub_scruct in struct.values():
		if isinstance(sub_scruct, dict):
			sub_key = is_key(sub_scruct, key, deep)
			if sub_key:
				break
	else:
		sub_key = None

	return sub_key


to_find = input('Значение какого ключа найти? ')
quest = input('Задать глубину? ').lower()
if quest == 'да':
	deepness = int(input('Введите глубину: '))
	find = is_key(site, to_find, deepness)
else:
	find = is_key(site, to_find)

print(find)
