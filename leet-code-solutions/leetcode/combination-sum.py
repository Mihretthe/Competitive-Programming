class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        answer = []
        combinations = []
        total = 0
        candidates.sort()

        def backtrack(index):
            nonlocal target, total

            if target == total:
                answer.append(combinations[:])
                return
            
            if total > target or (index < len(candidates) and candidates[index] > target):
                return 

            for i in range(index, len(candidates)):
                combinations.append(candidates[i])
                total += candidates[i]
                if total <= target:
                    backtrack(i)
                total -= combinations.pop()
        
        backtrack(0)
        return answer
