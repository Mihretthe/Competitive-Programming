class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        def inbound(row, col):
            return 0 <= row < rows and 0 <= col < cols

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        

        maxi = 0

        def dfs(row, col, value, visited):
            nonlocal maxi

            visited.add((row, col))
            for r, c in directions:
                newr = r + row
                newc = c + col

                if inbound(newr, newc) and (newr, newc) not in visited and grid[newr][newc] != 0:
                    maxi = max(maxi, value + grid[newr][newc])
                    dfs(newr, newc, value + grid[newr][newc], visited.copy())

        for i in range(rows):
            for j in range(cols):
                dfs(i, j, grid[i][j], set())

        return maxi
            