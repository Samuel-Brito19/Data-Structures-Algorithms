class ValuePair:
    def __init__(self, key, value) -> None:
        self.key = key
        self.value = value


class MyDictionary:
    def __init__(self, to_str_fn=str) -> None:
        self.to_str_fn = to_str_fn
        self.table: dict[str, ValuePair] = {}

    def set(self, key, value):
        if key is not None and value is not None:
            table_key = self.to_str_fn(key)
            self.table[table_key] = ValuePair(key, value)
            return True
        return False

    def get(self, key):
        value_pair = self.table.get(self.to_str_fn(key))
        return None if value_pair is None else value_pair.value

    def has_key(self, key):
        return self.table.get(self.to_str_fn(key)) is not None

    def remove(self, key):
        if self.has_key(key):
            del self.table[self.to_str_fn(key)]
            return True
        return False

    def key_values(self):
        return self.table.values()

    def values1(self):
        values = []
        for key_value in self.key_values():
            values.append(key_value.value)
        return values

    def values2(self):
        return list(map(lambda key_value: key_value.value, self.key_values()))

    def keys(self):
        keys = []
        for key_value in self.key_values():
            keys.append(key_value.key)
        return keys

    def for_each(self, callback_fn):
        value_pairs = self.key_values()
        for value_pair in value_pairs:
            result = callback_fn(value_pair.key, value_pair.value)
            if not result:
                break

    def is_empty(self):
        return self.__sizeof__ == 0

    def size(self):
        return len(self.table)

    def clear(self):
        self.table = {}

    def to_string(self):
        if self.is_empty():
            return ""
        value_pairs = self.key_values()
        obj_string = str(value_pairs[0])
        for pair in value_pairs:
            obj_string += str(pair)
        return obj_string


x = MyDictionary()
x.set("Gandalf", "gandalf@gmail.com")
x.set("Neymar", "neymar@gmail.com")
x.set("Messi", "messi@gmail.com")
print(x.has_key("Neymar"))
print(x.is_empty())
print(x.size())
