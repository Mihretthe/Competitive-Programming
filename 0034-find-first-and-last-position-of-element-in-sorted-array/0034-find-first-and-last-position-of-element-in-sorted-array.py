class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        """
        sorted array : nums
        finding the starting and ending of a target element
        checking the middle if the middle is the target check the next 
        [5,7,7,8,8,8,9]
        
        """
        l = 0
        r = len(nums) - 1
        left = -1
        right = -1
        while l <= r:
            m = (l + r)//2
            if nums[m] == target:
                left = m 
                right = m 
                while left > 0 and nums[left - 1] == target:
                    left -= 1
                while right < len(nums) - 1 and nums[right + 1] == target:
                    right += 1
                break
            elif nums[m] > target:
                r = m - 1
            else:
                l = m + 1
        return [left, right]