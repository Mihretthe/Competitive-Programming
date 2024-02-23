class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        rowMaxs = []
        colMaxs = []
        transpose_grid = list(zip(*grid))
        length = len(grid)

        for i in range(length):
            rowMaxs.append(max(grid[i]))
            colMaxs.append(max(transpose_grid[i]))

        max_sum = 0
        total = 0

        for i in range(length):
            for j in range(length):
                total += grid[i][j]
                max_sum += min(rowMaxs[i], colMaxs[j])

        return max_sum - total