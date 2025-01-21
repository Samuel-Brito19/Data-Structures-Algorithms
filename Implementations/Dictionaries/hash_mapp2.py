class ValuePair:
    def __init__(self, key, value) -> None:
        self.key = key
        self.value = value


class HashMap:
    def __init__(self, to_str_fn=str) -> None:
        self.to_str_fn = to_str_fn
        self.table: dict[str, ValuePair] = {}

    def lose_lose_hash_code(self, key):
        if isinstance(key, (int)):
            return key
        table_key = self.to_str_fn(key)
        hash_number = 0
        for i in range(len(table_key)):
            hash_number += ord(table_key[i])
        return hash_number % 37

    def hash_code(self, key):
        return self.lose_lose_hash_code(key)

    def put(self, key, value):
        if key is not None and value is not None:
            position = self.hash_code(key)
            self.table[position] = ValuePair(key, value)
            return True
        return False

    def get(self, key):
        value_pair = self.table.get(self.hash_code(key))
        return None if value_pair is None else value_pair.value

    def remove(self, key):
        hash_number = self.hash_code(key)
        value_pair = self.table[hash_number]
        if value_pair is not None:
            del self.table[hash_number]
            return True
        return False

    def get_table(self):
        return self.table

    def is_empty(self):
        return self.__sizeof__ == 0

    def size(self):
        return len(self.table)

    def clear(self):
        self.table = {}


x = HashMap()
x.put("messi", "messi@gmail.com")
x.put("mbappe", "mbappe@gmail.com")
x.put("neymar", "neymar@gmail.com")
print(x.hash_code("neymar"), "neymar")
print(x.hash_code("messi"), "messi")
print(x.hash_code("mbappe"), "mbappe")

print(x.get("neymar"))
print(x.get("saka"))
