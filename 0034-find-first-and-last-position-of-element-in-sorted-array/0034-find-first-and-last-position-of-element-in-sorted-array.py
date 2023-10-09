class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        if target not in set(nums):
            return [-1,-1]
        l = 0
        r = len(nums) - 1
        ans = []
        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                i = m
                while i >= 0 and nums[i] == target:
                    i -= 1
                ans.append(i + 1)
                i = m
                while i >= 0 and i < len(nums) and nums[i] == target:
                    i += 1
                ans.append(i - 1)
                return ans
            elif nums[m] > target:
                r -= 1
            else:
                l += 1
                
        
        
        
#         counter = Counter(nums)
#         if target not in counter:
#             return [-1,-1]
#         idx = nums.index(target)
#         return [idx, idx + counter[target] - 1]
        
        
        
    