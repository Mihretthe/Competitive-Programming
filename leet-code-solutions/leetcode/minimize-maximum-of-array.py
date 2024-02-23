class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        length = len(nums)
        running = 0
        mini_max = 0

        for i in range(length):
            running += nums[i]
            mini_max = max(mini_max, ceil(running / (i + 1)))

        return mini_max
