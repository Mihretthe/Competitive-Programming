class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        n = len(mat)
        m = len(mat[0])

        if r * c != n * m:
            return mat

        all_values = []
        for row in mat:
            all_values += row

        answer = []
        for i in range(0, n * m, c):
            answer.append(all_values[i: i + c])

        return answer

        