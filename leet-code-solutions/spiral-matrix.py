class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        first_row = 0
        last_row = len(matrix) - 1
        last_column = len(matrix[0]) - 1
        first_column = 0

        spiral = []
        visit = set([(0,i) for i in range(len(matrix[0]))])

        r = first_row
        l = last_column

        spiral += matrix[r]
        r += 1
        for _ in range(len(matrix[0])):
            print(spiral,r,l)
            
            while r <= last_row:
                if (r,l) not in visit:
                    spiral.append(matrix[r][l])
                    visit.add((r,l))
                r += 1
            
            first_row += 1
            
            r -= 1
            last_column -= 1
            l -= 1 
            while l >= first_column:
                if (r,l) not in visit:
                    spiral.append(matrix[r][l])
                    visit.add((r,l))
                l -= 1
                    
            l += 1
            last_row -= 1
            

            while r > first_row:
                r -= 1
                if (r,l) not in visit:
                    spiral.append(matrix[r][l])
                    visit.add((r,l))


             
            while l < last_column:
                l += 1
                if (r,l) not in visit:
                    spiral.append(matrix[r][l])
                    visit.add((r,l))
            first_column += 1   

            
            while r < last_row:
                r += 1
                if (r,l) not in visit:
                    spiral.append(matrix[r][l])
                    visit.add((r,l))
            
            print(spiral,r,l)
            if len(spiral) >= (len(matrix) * len(matrix[0])):
              return spiral
        return spiral

