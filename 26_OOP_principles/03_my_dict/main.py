class MyDict(dict):

    def get(self, key):
        if key not in self:
            return 0
        return self[key]


a = MyDict({'a': 1, 'b': 2})
print(a.get('c'))
print(a.get('a'))
