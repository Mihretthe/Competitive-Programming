class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        sorted_nums = sorted(set(nums))
        ans = 0
        indexes = {}
        for i in range(len(sorted_nums)):
            if sorted_nums[i] not in indexes:
                indexes[sorted_nums[i]] = i

        for i in range(len(nums)):
            ans += indexes[nums[i]]

        return ans

