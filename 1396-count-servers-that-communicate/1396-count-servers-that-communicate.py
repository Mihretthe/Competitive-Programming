class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        collect = set()
        n = len(grid)
        m = len(grid[0])

        

        for i in range(n):
            new = set()
            
            for j in range(m):
                if grid[i][j] == 1:
                    new.add((i, j))
            if len(new) > 1:
                collect.update(new)    



        for j in range(m):
            count = 0   
            new = set()         
            for i in range(n):
                if grid[i][j] == 1:                    
                    new.add((i, j))
            
            if len(new) > 1:
                collect.update(new)
        return len(collect)

        