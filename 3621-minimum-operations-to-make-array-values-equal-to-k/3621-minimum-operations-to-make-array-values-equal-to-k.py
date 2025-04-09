class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        
        my_set = set(nums)

        if min(my_set) < k:
            return -1

        if k in nums:
            return len(my_set) - 1
        else:
            return len(my_set) 
        