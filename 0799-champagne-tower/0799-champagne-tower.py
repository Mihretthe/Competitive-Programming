class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        a = [[0] * k for k in range(1,102)]
        a[0][0] = poured
        for i in range(query_row + 1):
            for j in range(i + 1):
                q = (a[i][j] - 1)/2
                if q > 0:
                    a[i + 1][j] += q        
                    a[i + 1][j + 1] += q
        return min(1,a[query_row][query_glass])
                    