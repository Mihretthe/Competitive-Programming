class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}

        for i in range(len(nums)):
            c = target - nums[i]
            if c in hashmap:
                return [i, hashmap[c]]

            hashmap[nums[i]] = i
