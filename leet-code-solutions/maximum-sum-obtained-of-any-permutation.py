class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        length = len(nums)
        prefix = [0] * length

        for start, end in requests:
            prefix[start] += 1
            if end + 1 < length:
                prefix[end + 1] -= 1
        for i in range(1, length):
            prefix[i] += prefix[i - 1]
        prefix.sort(reverse = True)
        nums.sort(reverse = True)
        max_sum = 0
        for num, pre in zip(nums, prefix):
            max_sum += (num * pre)



        return max_sum % (1000000007)