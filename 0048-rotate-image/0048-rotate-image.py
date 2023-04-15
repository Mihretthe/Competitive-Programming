class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        """
        swap :
            - i rows
                123
                456
                789
            - j columns
                147
                258
                369
            - what we do is changing the row to column and the column to row
        """
        b=[]
        j=0
        while j<len(matrix[0]):
            a=[]
            for i in matrix:
                a.append(i[j])
            b.append(a[::-1])
            j+=1
        for i in range(len(b)):
            matrix[i]=b[i]