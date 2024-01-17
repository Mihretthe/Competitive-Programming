class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        prefix = [1]
        suffix = [1]

        for index in range(1,length):
            prefix.append(prefix[-1] * nums[index - 1])
        for index in range(length - 2, -1, -1):
            suffix.append(suffix[-1] * nums[index + 1])
        for pre, suff in zip(prefix, suffix[::-1]):
            yield pre * suff