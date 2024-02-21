class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        
        unreachable = 1
        reachable = 0

        count_added = 0
        length = len(nums)
        
        index = 0
        while reachable < n:
            if index >= length:
                count_added += 1
                reachable += unreachable
                unreachable = reachable + 1
                continue
            if nums[index] > unreachable:   
                count_added += 1
                reachable += unreachable
                unreachable = reachable + 1
            elif nums[index] <= unreachable:
                reachable += nums[index]
                unreachable = reachable + 1
                index += 1

        return count_added