class LRUCache:
    def __init__(self, capacity: int):
        self.cache = {}
        self.cap = capacity

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        self.cache[key] = self.cache.pop(key)
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.pop(key)

        self.cache[key] = value
        if len(self.cache) > self.cap:
            self.cache.pop(next(iter(self.cache)))
