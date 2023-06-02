class MyHashMap:

    def __init__(self):
        global a
        a=dict()

    def put(self, key: int, value: int) -> None:
        global a
        a[key]=value
        

    def get(self, key: int) -> int:
        global a
        if key in a.keys():
            return a[key]
        return -1

    def remove(self, key: int) -> None:
        global a
        if key in a.keys():
            del a[key]


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)