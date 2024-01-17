class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        length = len(nums)
        for i in range(1, length):
            self.nums[i] += self.nums[i - 1]
        self.nums = [0] + self.nums
        

    def sumRange(self, left: int, right: int) -> int:
        return self.nums[right + 1] - self.nums[left]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)