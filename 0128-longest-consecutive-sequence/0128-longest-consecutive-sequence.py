class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # sort the array to hold the consecutive
        nums.sort()

        # a dictionary to count the numbers that are before
        hashmap = defaultdict(int)

        # iterate over the nums to collect the consecutives
        for num in nums:
            before = num - 1
            hashmap[num] = hashmap[before] + 1

        
        return max(hashmap.values()) if hashmap else 0