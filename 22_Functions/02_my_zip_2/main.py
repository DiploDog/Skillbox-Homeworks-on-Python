def shortest_sequence_range(*args):
      return range(len(sorted(args, key=len)[0]))


def zip_func(obj1, obj2):
      lst1 = list(obj1)
      lst2 = list(obj2)
      ans = ((lst1[i], lst2[i]) for i in shortest_sequence_range(obj1, obj2))
      return ans

object1 = {'a': 1, 'b': 2, 'c': 3}
#object1 = [1, 2, 3]
object2 = (10, 20, 30, 40)
object_zipped = zip_func(object1, object2)
print(object_zipped, '\n',
      list(object_zipped))
