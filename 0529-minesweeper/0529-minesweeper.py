class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        row, col = click
        if board[row][col] == 'M':
            board[row][col] = 'X'
            return board
        
        self.dfs(board, row, col)
        return board

    def dfs(self, board, row, col):
        if row < 0 or row >= len(board) or col < 0 or col >= len(board[0]) or board[row][col] != 'E':
            return
        
        mine_count = self.countAdjacentMines(board, row, col)
        
        if mine_count > 0:
            board[row][col] = str(mine_count)
            return
        board[row][col] = 'B'
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]
        for dr, dc in directions:
            new_row = row + dr
            new_col = col + dc
            self.dfs(board, new_row, new_col)

    def countAdjacentMines(self, board, row, col):
        mine_count = 0
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]
        for dr, dc in directions:
            new_row = row + dr
            new_col = col + dc
            if new_row >= 0 and new_row < len(board) and new_col >= 0 and new_col < len(board[0]) and board[new_row][new_col] == 'M':
                mine_count += 1
        return mine_count