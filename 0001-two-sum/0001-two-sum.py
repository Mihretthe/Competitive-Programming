class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # initialize a hashmap, to store the indices, also to look up a complement

        hashmap = {}

        length = len(nums)

        for i in range(length):
            num = nums[i]
            complement = target - num # calculating the complement

            # the condition to return the answer
            if complement in hashmap:
                return [i, hashmap[complement]]

            hashmap[num] = i