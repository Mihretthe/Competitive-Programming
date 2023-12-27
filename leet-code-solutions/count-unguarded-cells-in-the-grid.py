class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        grid = [['#'] * n for __ in range(m)]             

        for i, j in walls:
            grid[i][j] = "W"
        for i, j in guards:
            grid[i][j] = "G"

        for i, j in guards:
            # grid[i][j] = "G"

        
            for g in range(i + 1, m):
                if grid[g][j] == "W" or grid[g][j] == "G":
                    break
                grid[g][j] = "M"
            for g in range(i - 1, -1, -1):
                if grid[g][j] == "W" or grid[g][j] == "G":
                    break
                grid[g][j] = "M"
            for h in range(j - 1, -1, -1):
                if grid[i][h] == "W" or grid[i][h] == "G":
                    break
                grid[i][h] = "M"
            for h in range(j + 1,n):
                if grid[i][h] == "W" or grid[i][h] == "G":
                    break
                grid[i][h] = "M"
        
        result = []


        for i in grid:
            result.extend(i)
    
        return result.count("#")