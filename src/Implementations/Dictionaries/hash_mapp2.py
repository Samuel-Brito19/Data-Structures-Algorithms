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
