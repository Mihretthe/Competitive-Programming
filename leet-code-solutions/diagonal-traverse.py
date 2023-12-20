class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        sums = defaultdict(list)

        n = len(mat)
        m = len(mat[0])

        diagonal = []

        for i in range(n):
            for j in range(m):
                sums[i + j].append((i,j))
        for key, value in sums.items():
            if key % 2 == 0:
                value = value[::-1]

            for i, j in value:
                diagonal.append(mat[i][j])


        return diagonal

