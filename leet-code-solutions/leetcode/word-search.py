class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        
        def backtrack(i, j, index, visited):
            nonlocal word

            if index == len(word):
                return True
            
            if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]):
                return 
            
            if word[index] != board[i][j] or (i, j) in visited:
                return 
            
             
            visited.add((i,j))
            return backtrack(i - 1, j, index + 1,visited.copy()) or backtrack(i + 1, j, index + 1, visited.copy()) or backtrack(i, j + 1, index + 1, visited.copy()) or backtrack(i, j - 1, index + 1, visited.copy())
        

        for i in range(len(board)):
            for j in range(len(board[0])):
                if word[0] == board[i][j]:
                    if backtrack(i, j, 0,set()):
                        return True
            
                       