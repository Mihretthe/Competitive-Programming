class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        answer = 0
        path = []
        length = len(nums)
        intended = 0

        for num in nums:
            intended |= num

        def calc(path):
            intended = 0
            for p in path:
                intended |= p
            return intended


        def backtrack(index):
            nonlocal answer
            if calc(path) == intended:
                # print("me")
                answer += 1
            # print(path, index, calc(path) == (intended))
            if index == length:
                return
            
            
            for i in range(index, length):
                path.append(nums[i])
                backtrack(i + 1)
                path.pop()
        
        backtrack(0)

        return answer
            
            
            