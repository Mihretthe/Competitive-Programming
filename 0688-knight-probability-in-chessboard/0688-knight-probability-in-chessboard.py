class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        """
        Count the number of stays
        """

        dxns = [(1, 2), (2, 1), (-2, 1), (-1, 2), (-2, -1), (-1, -2),(2, -1), (1, -2)]
        
        

        def inbound(row, col):
            return 0 <= row < n and 0 <= col < n

        memo = {}

        
        def dp(moves, ro, col):
            if (ro, col, moves) in memo:
                return memo[(ro, col, moves)]
            if moves == 0:
                if ro == row and col == column:
                    return 1 
                else:
                    return 0
            
            count = 0
            for r, c in dxns:
                newr = r + ro
                newc = c + col
                
                if inbound(newr, newc):         
                    count += (dp(moves - 1, newr, newc))
            
            memo[(ro, col, moves)] = count / 8
            return memo[(ro, col, moves)]

        answer = 0

        for i in range(n):
            for j in range(n):
                answer += dp(k, i, j)

        return answer

                    