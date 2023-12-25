class Bitset:

    def __init__(self, size: int):
        self.bitset = ["0"] * size
        self.flipped = ["1"] * size
        self.size = size
        self.counter = 0        

    def fix(self, idx: int) -> None:
        if self.bitset[idx] == "0":
            self.bitset[idx] = "1"
            self.flipped[idx] = "0"
            self.counter += 1       

    def unfix(self, idx: int) -> None:
        if self.bitset[idx] == "1":
            self.bitset[idx] = "0"
            self.flipped[idx] = "1"
            self.counter -= 1        

    def flip(self) -> None:
        self.bitset, self.flipped = self.flipped, self.bitset
        self.counter = self.size - self.counter        

    def all(self) -> bool:
        return self.counter == self.size
        

    def one(self) -> bool:
        return self.counter
        

    def count(self) -> int:
        return self.counter
        

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