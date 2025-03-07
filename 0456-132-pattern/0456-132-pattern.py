class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        
        length = len(nums)
        previous_minimum = [inf]
        mini = nums[0]
        for i in range(1, length):
            mini = min(mini, nums[i])
            previous_minimum.append(mini)
        
        stack = []
        for i in range(length - 1, -1, -1):
            while stack and stack[-1] < nums[i]:
                num = stack.pop()
                if num > previous_minimum[i]:
                    return True
            stack.append(nums[i])

        
        return False