class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for k in range(0, 9, 3):
            collect = set()
            for i in range(k,k+3):
                for j in range(3):
                    if board[i][j] != "." and board[i][j] in collect:
                        return False
                    collect.add(board[i][j])

        for k in range(0, 9, 3):
            collect = set()
            for i in range(k,k+3):
                for j in range(3,6):
                    if board[i][j] != "." and board[i][j] in collect:
                        return False
                    collect.add(board[i][j])

        for k in range(0, 9, 3):
            collect = set()
            for i in range(k,k+3):
                for j in range(6,9):
                    if board[i][j] != "." and board[i][j] in collect:
                        return False
                    collect.add(board[i][j])

        for row in board:
            counter = Counter(row)
            counter.pop(".")
            c = list(counter.values())
            if c.count(1) != len(counter):
                return False

        for row in zip(*board):
            counter = Counter(row)
            counter.pop(".")
            c = list(counter.values())
            if c.count(1) != len(counter):
                return False
            
        return True














