class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        
        answer = set()
        path = []
        total = 0

        def backtrack(num):
            nonlocal n, k, total
            if len(path) == k and total == n:
                answer.add(tuple(path[:]))
                return 


            for i in range(num, 10):
                path.append(i)
                total += i
                if total <= n:
                    backtrack(i + 1)
                total -= path.pop()
        
        backtrack(1)
        return answer
            



