class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        n = len(nums)
        if n == 3:
            return sum(nums)
        nums.sort()
        ans = sum(nums[:3])
        
        for i in range(n):
            l = i + 1
            r = n - 1
            
            while l < r:                
                if (nums[i] + nums[l] + nums[r]) == target:                    
                    return target
                if abs(target - (nums[i] + nums[l] + nums[r])) < abs(target - ans):
                    ans =( nums[i] + nums[l] + nums[r])
                if ( nums[i] + nums[l] + nums[r]) < target:
                    l += 1
                else:
                    r -= 1
               
                    
                
        return ans