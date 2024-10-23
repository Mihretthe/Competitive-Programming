class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        
        length = len(nums)
        count = 0

        for i in range(length):
            for j in range(i + 1, length):
                for k in range(j + 1, length):
                    if nums[k] - nums[j] == nums[j] - nums[i] == diff:
                        count += 1

        return count