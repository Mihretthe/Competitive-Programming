class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        
        dxn = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        rows = len(grid)
        cols = len(grid[0])

        def inbound(row, col):
            return 0 <= row < rows and 0 <= col < cols

        visited = [[False for i in range(cols)] for j in range(rows)]
        
        def dfs(row, col):
            # print(row, col, grid[row][col])
            visited[row][col] = True

            if not inbound(row, col):
                return 0
            
            if grid[row][col] == 0:
                return 0
            
            total = 0

            for r, c in dxn:
                newr = r + row
                newc = c + col

                if inbound(newr, newc) and not visited[newr][newc]:
                    visited[newr][newc] = True
                    total += grid[newr][newc] + dfs(newr, newc)
                    
            return total

        
        
        maxi = 0

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] != 0 and not visited[i][j]:
                    maxi = max(maxi, grid[i][j] + dfs(i, j))


        return maxi


