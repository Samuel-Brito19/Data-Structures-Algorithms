class MyDictionary:
    def __init__(self):
        self.items = {}

    def set(self, key, value):
        self.items[key] = value

    def get(self, key):
        return self.items.get(key)

    def remove(self, key):
        if key in self.items:
            del self.items[key]

    def keys(self):
        return list(self.items.keys())

    def values(self):
        return list(self.items.values())

    def items(self):
        return list(self.items.items())

    def has_key(self, key):
        return key in self.items

    def clear(self):
        self.items.clear()

    def size(self):
        return len(self.items)


test = MyDictionary()
test.set('neymar', 'craque')
test.set('messi', 'argentina')
print(test.has_key('neymar'))
print(test.keys())
print(test.values())
print(test.get('messi'))