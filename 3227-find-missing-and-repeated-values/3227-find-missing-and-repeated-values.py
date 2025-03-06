class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        length = (n * n + 1)
        answer = []
        my_set = set()
        for i in range(n):
            for j in range(n):
                if grid[i][j] in my_set:
                    answer.append(grid[i][j])
                my_set.add(grid[i][j])
                
        for i in range(1, length):
            if i not in my_set:
                answer.append(i)
        
        return answer