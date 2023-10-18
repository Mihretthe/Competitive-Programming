class MedianFinder:

    def __init__(self):
        self.nums = []

    def addNum(self, num: int) -> None:
        bisect.insort(self.nums,num)

    def findMedian(self) -> float:
        n = len(self.nums)
        if n % 2 == 0:
            n = n//2
            return (self.nums[n - 1] + self.nums[n] ) / 2
        else:
            n = n // 2
            return self.nums[n]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()