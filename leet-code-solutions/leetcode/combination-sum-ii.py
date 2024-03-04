class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        combinations = []
        answer = set()
        total = 0
        candidates.sort()
 
        def backtrack(index, prev):
            nonlocal total, target

            if total == target:
                answer.add(tuple(combinations[:]))

            if total > target or (index < len(candidates) and (candidates[index] > target or prev == candidates[index])):
                return 
             
            for i in range(index, len(candidates)):
                combinations.append(candidates[i])
                total += candidates[i]
                if total <= target:
                    backtrack(i + 1, prev)
                prev = combinations.pop()
                total -= prev

        backtrack(0, -1)
        return answer
                
