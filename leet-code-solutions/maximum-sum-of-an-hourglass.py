class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        """
        from row 1 - n - 2
        from column 1 - n - 2
        """

        n = len(grid)
        m = len(grid[0])

        dxn = [[-1,-1], [-1,0], [-1,1], [0,0], [1,-1], [1,0], [1,1]]

        max_sum = 0
      
        for i in range(1, n - 1):
            for j in range(1, m - 1):
                s = 0
                for r, c in dxn:
                    r += i
                    c += j                    
                    s += grid[r][c]

                max_sum = max(s, max_sum)

        return max_sum

                


