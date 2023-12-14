class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        transpose = list(zip(*grid))        
        n = len(grid)
        m = len(transpose)
        diff = []
        

        for i in range(n):
            one_count = grid[i].count(1)
            zero_count = m - one_count
            diff.append([one_count - zero_count] * m)
        
        for_reverse = []
        for i in range(m):
            one_count = transpose[i].count(1)
            zero_count = n - one_count
            for_reverse.append([one_count - zero_count] * n)
        
        for_reverse = list(zip(*for_reverse))

        result = [[diff[i][j] + for_reverse[i][j] for j in range(m)] for i in range(n)]

            

        return result