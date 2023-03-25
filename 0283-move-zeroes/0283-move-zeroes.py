class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        r=len(nums)-1
        l=0
        while l<r:
            if nums[l]==0:
                for j in range(l,r):
                    nums[j]=nums[j+1] 
                nums[r]=0
                r-=1
            else:
                l+=1
                
        