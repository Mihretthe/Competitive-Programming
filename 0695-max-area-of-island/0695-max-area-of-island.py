class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        max_area = 0

        visited = set()

        def dfs(row, col):
            nonlocal visited
            if 0 <= row < rows and 0 <= col < cols and grid[row][col] == 1 and (row, col) not in visited:
                visited.add((row, col))
                area = 1

                area += dfs(row + 1, col)  
                area += dfs(row - 1, col)
                area += dfs(row, col + 1)
                area += dfs(row, col - 1) 

                return area

            return 0

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1 and (i, j) not in visited:
                    max_area = max(max_area, dfs(i, j))

        return max_area