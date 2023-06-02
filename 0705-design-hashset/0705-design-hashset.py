class MyHashSet:

    def __init__(self):
        global a
        a=set()
        

    def add(self, key: int) -> None:
        global a
        a.add(key)

    def remove(self, key: int) -> None:
        global a
        if key in a:
            a.remove(key)

    def contains(self, key: int) -> bool:
        global a
        return key in a

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)