class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        y=list()
        for i in range(len(nums)):
            y.append(int(nums[i]))
        y.sort(reverse=True)
        x=str(y[k-1])
        return x
        
        