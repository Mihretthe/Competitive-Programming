class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:

        ans = []

        for j in range(len(matrix[0])):
            row = []
            for i in range(len(matrix)):
                row.append(matrix[i][j])
            ans.append(row)

        return ans