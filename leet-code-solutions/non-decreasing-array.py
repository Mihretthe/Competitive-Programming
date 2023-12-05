class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        
        for i in range(1,len(nums)):
            if i > 0 and i < len(nums) - 1:
                if nums[i - 1] > nums[i] and nums[i + 1] < nums[i - 1]:
                    nums[i - 1] = nums[i]
                    break
                elif nums[i - 1] > nums[i] and nums[i + 1] >= nums[i - 1]:
                    print("me")
                    nums[i] = nums[i - 1]
                    break
                
            elif i == len(nums) - 1:
                if nums[i - 1] > nums[i]:
                    nums[i] = nums[i - 1]
                    break
        
        print(nums)
            
        return sorted(nums) == nums