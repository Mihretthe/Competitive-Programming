class Solution:
    def arraySign(self, nums: List[int]) -> int:
        if 0 in nums:
            return 0 
        x=[i for i in nums if i<0]
        if len(x)%2==0:
            return 1
        else:
            return -1
    