class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        prefix = [nums[0]]
        length = len(nums)
        for i in range(1, length):
            prefix.append(prefix[-1] + nums[i])
        
        answer = 0
        for i in range(length - 1):
            if prefix[i] >= prefix[-1] - prefix[i]:

                answer += 1
        
        return answer