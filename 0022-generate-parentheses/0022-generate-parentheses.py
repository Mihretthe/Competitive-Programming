class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        
        def backtrack(n):
            if n == 0:
                return [""]
            parenthesis = []
            
            for i in range(n):
                
                inner = backtrack(i)
                outer = backtrack(n-i-1)
                for j in inner:
                    for k in outer:
                        parenthesis.append(f'({j}){k}')
            return parenthesis
        return backtrack(n)