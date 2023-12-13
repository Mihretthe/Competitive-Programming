class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        column_wise = []
        count = 0

        for i in range(len(mat[0])):
            column = []
            for j in range(len(mat)):
                column.append(mat[j][i])

            column_wise.append(column)

        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 1:
                    if mat[i].count(1) == 1 and column_wise[j].count(1) == 1:
                        count += 1
        
        return count

