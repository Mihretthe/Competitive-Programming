class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        answer = []
        path = []

        def backtrack(index):
            if len(path) == len(nums):
                answer.append(path[:])
                return 

            for i in range(len(nums)):
                if nums[i] in path:
                    continue
                path.append(nums[i])
                backtrack(i + 1)
                path.pop()

        backtrack(0)
        return answer