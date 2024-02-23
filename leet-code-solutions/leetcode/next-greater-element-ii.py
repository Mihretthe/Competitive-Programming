class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        length = len(nums)       
        
        answer = [-1] * length
        stack = []

        for i in range(length * 2):

            while stack and nums[stack[-1]] < nums[i % length]:
                answer[stack.pop()] = nums[i % length]

            stack.append(i % length)

        return answer

