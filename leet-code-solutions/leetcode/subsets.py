class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        answer = []
        path = []

        def backtrack(i):
            answer.append(path[:])

            for j in range(i, len(nums)):
                path.append(nums[j])
                backtrack(j + 1)
                path.pop()

        backtrack(0)
        return answer
