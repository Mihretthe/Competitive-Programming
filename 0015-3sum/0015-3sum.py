class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        hashmap = defaultdict(list)
        n = len(nums)
        ans = []
        nums.sort()
        
        
        for i in range(n):
            if nums[i] in hashmap:
                continue
            l = i  
            r = n - 2
            new = nums[:i] + nums[i+1:]
            
            while l < r:                
                if new[l] + new[r] == (-1 * nums[i]) :
                    
                    if sorted([new[l],new[r], nums[i]])  not in hashmap[nums[i]] and sorted([new[l],new[r], nums[i]])  not in ans:
                        hashmap[nums[i]].append(sorted([new[l],new[r], nums[i]]))
                    r -= 1                
                elif new[l] + new[r] < (-1 * nums[i]):
                    l += 1
                elif new[l] + new[r] > (-1 * nums[i]):
                    r -= 1
                else:
                    l += 1
                
            ans += hashmap[nums[i]]
        return ans
        
    
