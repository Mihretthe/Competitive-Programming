class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        i=0
        c=0
        
        while i<len(grid):
            r=[]
            for j in range(len(grid)):
                r.append(grid[j][i])             
            if r in grid:
                c+=grid.count(r)
            i+=1
        return c