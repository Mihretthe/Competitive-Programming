class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def check(matrix):
            my_set = set()
            count = 0
            for i in range(9):
                for j in range(9):
                    if matrix[i][j] == ".":
                        continue
                    count += 3
                    my_set.add((i//3, j//3, matrix[i][j]))
                    my_set.add((i,matrix[i][j],"row"))
                    my_set.add((j,matrix[i][j],"col"))
            
            return len(my_set) == count
        
        return check(board)