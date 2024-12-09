class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        
        curr = nums[0] % 2

        for num in nums[1:]:
            if num % 2 == curr:
                return False
            curr = num % 2
        return True