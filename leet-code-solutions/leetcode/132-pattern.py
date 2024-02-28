class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack = []
        length = len(nums)
        minimum = nums[0]

        for i in range(length):
            while stack and nums[i] >= stack[-1][0]:
                stack.pop()
            
            if stack and nums[i] > stack[-1][1]:
                return True

            stack.append((nums[i], minimum))
            minimum = min(nums[i], minimum)
        
        return False