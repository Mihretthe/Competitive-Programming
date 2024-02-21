class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        rows = len(matrix) + 1
        cols = len(matrix[0]) + 1

        prefix = [[0 for _ in range(cols)] for __ in range(rows)]

        for i in range(1, rows):
            for j in range(1, cols):
                r = i - 1
                c = j - 1
                prefix[i][j] = matrix[r][c] + prefix[i][c] + prefix[r][j] - prefix[r][c]
                
        submatrices = 0
        for k in range(1,rows):            
            for i in range(k, rows):
                hashmap = defaultdict(int)
                hashmap[0] = 1
                pre_sum = 0
                for j in range(1, cols):
                    pre_sum = (prefix[i][j] - prefix[k - 1][j])
                    submatrices += hashmap[pre_sum - target]
                    hashmap[pre_sum] += 1
                
        return submatrices