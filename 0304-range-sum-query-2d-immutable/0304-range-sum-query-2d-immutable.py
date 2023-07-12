class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        self.prefix = [[0 for i in range(len(matrix[0])+1)]]
        for i in self.matrix:
            temp=[0]
            for j in i:
                if temp:
                    temp.append( temp[-1]+j)
                else:
                    temp.append(j)
            self.prefix.append(temp)
        for i in range(len(self.prefix[0])):
            for j in range(len(self.prefix)):
                if j-1>=0:
                    self.prefix[j][i]+=self.prefix[j-1][i]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.prefix[row2+1][col2+1]-self.prefix[row2+1][col1]-self.prefix[row1][col2+1]+self.prefix[row1][col1]


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)