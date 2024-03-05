class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        answer = []
        path = []

        def backtrack(open, close):
            if open == close == n:
                answer.append("".join(path[:]))
            
            if open < n:
                path.append("(")
                backtrack(open + 1, close)
                path.pop()

            if close < open:
                path.append(")")
                backtrack(open, close + 1)
                path.pop()
            
        backtrack(0,0)
        return answer

            
