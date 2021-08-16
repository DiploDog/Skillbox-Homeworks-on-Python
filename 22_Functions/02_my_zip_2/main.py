def zip_func(obj1=list, obj2=list):
    return ((obj1[i], obj2[i])
            for i in range(min(len(obj1), len(obj2))))


#object1 = {'a': 1, 'b': 2, 'c': 3}
object1 = [1, 2, 3]
object2 = (10, 20, 30, 40)
object_zipped = zip_func(object1, object2)
print(object_zipped, '\n',
      list(object_zipped))
