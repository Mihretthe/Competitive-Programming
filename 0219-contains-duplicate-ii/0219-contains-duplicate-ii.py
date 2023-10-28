class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hashmap = {}
        for i in range(len(nums)):
            if nums[i] in hashmap:
                hashmap[nums[i]][0] += 1  
                if hashmap[nums[i]][0] > 1 and abs(i - hashmap[nums[i]][1]) <= k:
                    return True
                hashmap[nums[i]][1] = i

            else:
                hashmap[nums[i]] = [1, i]
            
        return False
                
                
                