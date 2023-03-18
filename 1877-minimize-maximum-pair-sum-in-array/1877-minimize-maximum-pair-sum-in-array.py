class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        l=0
        nums.sort()
        a=list()
        r=len(nums)-1
        while(l<r):
            a.append(nums[l]+nums[r])
            l+=1
            r-=1
        x=max(a)
        return x
    