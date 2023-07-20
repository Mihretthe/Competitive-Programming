class LRUCache:

    def __init__(self, capacity: int):
        self.store = {}
        self.recently = []
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key in self.store.keys():
            if key in self.recently:
                self.recently.remove(key)
            self.recently.append(key)
            return self.store[key]
        return -1

    def put(self, key: int, value: int) -> None:
        if key not in self.store.keys() and len(self.store) >= self.capacity:
            del self.store[self.recently[0]]
            self.recently = self.recently[1:]
        self.store[key] = value
        if key in self.recently:
            self.recently.remove(key)
        self.recently.append(key)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)