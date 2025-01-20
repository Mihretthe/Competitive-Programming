class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        n = len(matrix)

        for i in range(n):
            
            total = set()
            for j in range(n):
                total.add(matrix[i][j])
            if len(total) != n:
                return False
        for j in range(n):
            
            total = set()
            for i in range(n):
                total.add(matrix[i][j])
            if len(total) != n:
                return False
        
        return True
