class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:

        indexes = {}

        for i in range(len(nums)):
            indexes[nums[i]] = i

        for key, val in operations:
            if key in indexes:
                indexes[val] = indexes[key]
                nums[indexes[key]] = val
                
        

        return nums

