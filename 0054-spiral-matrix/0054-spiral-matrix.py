class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        rows = len(matrix)
        cols = len(matrix[0])
        top = 0 
        bottom = rows - 1
        left = 0
        right = cols - 1

        answer = []

        while top <= bottom and left <= right:
            
            j = left
            while j <= right and len(answer) < rows * cols:
                answer.append(matrix[top][j])
                j += 1
            
            top += 1
            
            j = top
            while j <= bottom and len(answer) < rows * cols:
                answer.append(matrix[j][right])
                j += 1   
            

            right -= 1
            
            
            j = right
            while j >= left and len(answer) < rows * cols:
                answer.append(matrix[bottom][j])
                j -= 1
            bottom -= 1
            
            
            j = bottom
            while j >= top and len(answer) < rows * cols:
                answer.append(matrix[j][left])
                j -= 1
            left += 1
            

        return answer        