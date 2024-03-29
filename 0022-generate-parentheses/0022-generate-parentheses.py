class Solution:
    def generateParenthesis(self, n: int) -> List[str]:       
        if n == 0:
            return [""]
        parenthesis = []
        for i in range(n):
            inner = self.generateParenthesis(i)
            outer = self.generateParenthesis(n-i-1)
            for j in inner:
                for k in outer:
                    parenthesis.append(f'({j}){k}')
        return parenthesis