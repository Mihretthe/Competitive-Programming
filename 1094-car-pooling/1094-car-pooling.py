class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        def ending(nums):
            return nums[2]
        trips.sort(key = ending)
        max_end = trips[-1][2]
        counting = [0] * (max_end)
        contain = set()
        for i in trips:
            per, start, end = i
            for j in range(start, end ):
                counting[j - 1] += per 
                if counting[j - 1] > capacity:
                    return False
        return True
                
            