class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        ans = []
        for i in range(len(nums)):    
            for j in range(i + 1,len(nums)):
                l = j + 1
                r = len(nums) - 1
                s = target - nums[i] - nums[j]
                while l < r:
                    if nums[l] + nums[r] == s:
                        if [nums[i],nums[j], nums[l],nums[r]] not in ans:
                            ans.append([nums[i],nums[j], nums[l],nums[r]])
                        r -= 1
                    elif nums[l] + nums[r] < s: 
                        l += 1
                    elif nums[l] + nums[r] > s:
                        r -= 1
        return ans

                    

        