class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        a = nums[0]
        b = float('inf')
        
        for i in range(1, len(nums)):
            if a > nums[i] and b > nums[i]:
                a = nums[i]
            elif a < nums[i] and b > nums[i]:
                b = nums[i]
            elif b < nums[i]:
                return True

        return False
        
        


        return False

