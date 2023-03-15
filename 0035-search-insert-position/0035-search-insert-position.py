class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l=0
        found=False
        r=len(nums)-1
        while l<r:
            m=int((l+r)/2)
            if nums[m]==target:
                found=True
                return m
            elif nums[m]>target:
                r=m-1
            elif nums[m]<target:
                l=m+1
        if found==False:
            nums.append(target)
            nums.sort()
            return nums.index(target)
                