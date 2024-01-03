class Solution:
    def removeDuplicates(self, nums: List[int]):
        l = 0
        r = 1
        n = len(nums)
        count = 0

        while l < n and r < n:
            if nums[l] == nums[r]:
                nums[r] = 101
                r += 1
                count += 1
            else:
                l = r
                r += 1
   
        nums.sort() 
 
          
        return n - count