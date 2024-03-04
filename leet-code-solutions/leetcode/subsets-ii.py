class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        answer = []
        path = []
        nums.sort()

        def backtrack(index, prev):
            if index < len(nums) and nums[index] == prev:
                return
            if path[:] in answer:
                return 
            answer.append(path[:]) 

            for i in range(index, len(nums)):
                path.append(nums[i])
                backtrack(i + 1, prev)
                prev = path.pop()

        backtrack(0, -11)
        return answer
