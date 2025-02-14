class ProductOfNumbers:

    def __init__(self):
        self.nums = []
        self.product = 1

    def add(self, num: int) -> None:
        if num == 0:
            self.nums = []
            return
        if self.nums:
            self.nums.append(self.nums[-1] * num)
        else:
            self.nums.append(num)

        

    def getProduct(self, k: int) -> int:
        if not self.nums:
            return 0
        index = len(self.nums) - k - 1
        if index >= 0:
            return self.nums[-1] // self.nums[index]
        elif index == -1:
            return self.nums[-1]
        return 0


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)