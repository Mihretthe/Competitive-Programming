class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        answer = []
        path = []

        def backtrack(index):
            nonlocal n, k

            if len(path) == k:
                answer.append(path[:])
                return
            
            for i in range(index, n + 1):
                path.append(i)
                backtrack(i + 1)
                path.pop()

        backtrack(1)

        return answer