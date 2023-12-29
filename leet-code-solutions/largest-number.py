class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def helper(s, s1):
            s = str(s)
            s1 = str(s1)
            return int(s1 + s) > int(s + s1)

        for i in range(len(nums)):
            for j in range(len(nums) - 1 - i):
                if helper(nums[j], nums[j + 1]):
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]

        nums = list(map(str, nums))

        return str(int("".join(nums)))