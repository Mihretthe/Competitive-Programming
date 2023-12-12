class OrderedStream:

    def __init__(self, n: int):
        self.n = n
        self.hashmap = {}

    def insert(self, idkey: int, value: str) -> List[str]:
        self.hashmap[idkey] = value
        
        result = []
        for i in range(1,idkey):
            if i not in self.hashmap:
                return []
        while idkey in self.hashmap:
            result.append(self.hashmap[idkey])
            idkey += 1
        return result


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)