class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        length = len(nums)

        answer = []
        path = []

        def backtrack(index):
            if len(path) > 1 and path not in answer:
                answer.append(path[:]) 
            if index == length:
                return 

            for i in range(index, length):
                if not path:
                    path.append(nums[index])
                    backtrack(i + 1)
                    path.pop()
                elif nums[index] >= path[-1]:
                    path.append(nums[index])
                    backtrack(i + 1)
                    path.pop()
        for i in range(length):
            backtrack(i)
            
        return answer