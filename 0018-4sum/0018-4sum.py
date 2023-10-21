class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []
        
        nums.sort()
        
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                l, r = j + 1, len(nums) - 1
                remaining = target - (nums[i] + nums[j])
                
                while l < r:
                    if nums[l] + nums[r] == remaining:
                        if sorted([nums[i], nums[j], nums[l], nums[r]]) not in ans:
                            ans.append(sorted([nums[i], nums[j], nums[l], nums[r]]))
                        l += 1
                    elif nums[l] + nums[r] < remaining:
                        l += 1
                    elif nums[l] + nums[r] > remaining:
                        r -= 1
                        
        return ans
                