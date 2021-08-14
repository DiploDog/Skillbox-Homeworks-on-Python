def zip_func(obj1, obj2):

    obj1 = list(obj1) if type(obj1) != list else obj1
    obj2 = list(obj2) if type(obj2) != list else obj2

    if len(obj1) > len(obj2):
        obj1 = obj1[:len(obj2)]

    init_obj = obj1.copy()
    obj1.extend(obj2)

    zipped = ((obj1[i], obj1[i + len(init_obj)]) for i in range(0, len(init_obj)))

    return zipped, list(zipped)


object1 = 'abcd'
object2 = (10, 20, 30, 40)
gen, object_zipped = zip_func(object1, object2)

print(f'Результат:\n{gen}')
for tpl in object_zipped:
    print(tpl)
