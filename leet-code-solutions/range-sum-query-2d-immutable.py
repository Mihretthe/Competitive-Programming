class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        n, m = len(matrix), len(matrix[0])
        prefix = [[0 for _ in range(m + 1)] for __ in range(n + 1)] 
        for i in range(1,n + 1):
            for j in range(1,m + 1):
                prefix[i][j] = prefix[i - 1][j] + prefix[i][j - 1] + matrix[i - 1][j - 1] - prefix[i - 1][j - 1]
        self.prefix = prefix


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        prefix = self.prefix
        row1 += 1
        row2 += 1
        col2 += 1
        col1 += 1
        return prefix[row2][col2] - prefix[row2][col1 - 1] - prefix[row1 - 1][col2] + prefix[row1 - 1][col1 - 1]

        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)