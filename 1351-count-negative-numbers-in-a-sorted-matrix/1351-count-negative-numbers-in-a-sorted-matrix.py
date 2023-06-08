class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        m=0
        n=0
        c=0
        while m<len(grid):
            if grid[m][n]<0:
                c+=1
            n+=1
            if n==len(grid[0]):
                n=0
                m+=1
        return c
                
            