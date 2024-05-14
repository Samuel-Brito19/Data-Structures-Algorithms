class ValuePair:
    def __init__(self, key, value) -> None:
        self.key = key
        self.value = value


class HashMap:
    def __init__(self, to_str_fn=str) -> None:
        self.to_str_fn = to_str_fn
        self.table: dict[str, ValuePair] = {}
