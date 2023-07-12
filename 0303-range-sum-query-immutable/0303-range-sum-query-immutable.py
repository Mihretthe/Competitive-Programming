class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.prefix = []
        for num in nums:
            if self.prefix:
                self.prefix.append( num + self.prefix[-1])
            else:
                self.prefix.append( num )

    def sumRange(self, left: int, right: int) -> int:
        if left==0:
            return self.prefix[right]
        return self.prefix[right] - self.prefix[left-1]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)