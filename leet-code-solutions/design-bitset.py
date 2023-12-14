class Bitset:

    def __init__(self, size: int):
        self.bitset = ["0"] * size
        self.flipped = ["1"] * size
        self.size = size
        self.counter = {"0":size, "1":0}
        self.counter_flipped = {"0":0, "1":size}

    def fix(self, idx: int) -> None:
        if self.bitset[idx] == "0":
            self.bitset[idx] = "1"
            self.flipped[idx] = "0" 
            self.counter["1"] += 1
            self.counter["0"] -= 1
            self.counter_flipped["1"] -= 1  
            self.counter_flipped["0"] += 1

    def unfix(self, idx: int) -> None:
        if self.bitset[idx] == "1":
            self.bitset[idx] = "0"
            self.flipped[idx] = "1" 
            self.counter["1"] -= 1
            self.counter["0"] += 1  
            self.counter_flipped["0"] -= 1  
            self.counter_flipped["1"] += 1  
        

    def flip(self) -> None:
        self.bitset, self.flipped = self.flipped, self.bitset
        self.counter, self.counter_flipped = self.counter_flipped, self.counter
        

    def all(self) -> bool:
        return self.counter["1"] == self.size
        

    def one(self) -> bool:
        return self.counter["1"]

    def count(self) -> int:
        return self.counter["1"]

    def toString(self) -> str:
        return "".join(self.bitset)
        


# Your Bitset object will be instantiated and called as such:
# obj = Bitset(size)
# obj.fix(idx)
# obj.unfix(idx)
# obj.flip()
# param_4 = obj.all()
# param_5 = obj.one()
# param_6 = obj.count()
# param_7 = obj.toString()