class RandomizedSet:

    def __init__(self):
        self.randomset = []
        self.random_set = {}

    def insert(self, val: int) -> bool:
        if val in self.random_set:
            return False
        self.randomset.append(val)
        self.random_set[val] = len(self.randomset) - 1
        return True
        

    def remove(self, val: int) -> bool:
        if val in self.random_set:
            last_val =  self.randomset[-1]
            self.randomset[-1], self.randomset[self.random_set[val]] = self.randomset[self.random_set[val]], self.randomset[-1]
            self.random_set[last_val], self.random_set[val] =  self.random_set[val], self.random_set[last_val]
            self.randomset.pop()
            del self.random_set[val]
            return True
        return False
        

    def getRandom(self) -> int:
        
        random_number = random.randint(0,len(self.randomset) - 1)
        return self.randomset[random_number]
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()