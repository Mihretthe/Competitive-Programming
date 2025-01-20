class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        rows = len(mat)
        cols = len(mat[0])
        length = len(arr)

        
        rowDict = {i + 1: cols for i in range(rows)}
        colDict = {i + 1: rows for i in range(cols)}
        place = {}

        for i in range(rows):
            for j in range(cols):
                place[mat[i][j]] = (i + 1, j + 1)

       

        for i in range(length):
            val = arr[i]
            rowDict[place[val][0]] -= 1
            if rowDict[place[val][0]] == 0:
                return i 
            
            colDict[place[val][1]] -= 1
            if colDict[place[val][1]] == 0:
                return i
        

        return ans
            

