class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        s=sum(nums)
        l="".join([str(i) for i in nums])
        w=0
        for i in l:
            w+=int(i)
        return abs(w-s)