class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:        
        l=len(grid[0])-1
        ans=0
        while l>=0:
            a=[]
            for i in grid:
                a.append(max(i))
                i.remove(max(i))
            ans+=max(a)
            l-=1         
        return ans
    