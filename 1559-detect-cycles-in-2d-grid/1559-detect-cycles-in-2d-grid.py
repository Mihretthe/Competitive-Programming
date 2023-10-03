class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
#         rows = len(grid)
#         cols = len(grid[0])
#         visit = set()

#         def cycle(i, j, visited, n):
#             dxn = [[0, 1], [1, 0], [-1, 0], [0, -1]]
#             nonlocal visit

#             if (i, j) in visited:
#                 return False

#             visited.add((i, j))

#             for d in dxn:
#                 r = i + d[0]
#                 c = j + d[1]

#                 if r >= 0 and r < rows and c >= 0 and c < cols:
#                     if grid[r][c] == grid[i][j] and (r, c) not in visited:
#                         if cycle(r, c, visited, n):
#                             return True

#                 else:
#                     visit.add((i, j))
#                     return False

#             return False

#         for i in range(rows):
#             for j in range(cols):
#                 n = (i, j)

#                 if cycle(i, j, set(), n):
#                     return True

#         return False
        
        visited, visited_cur = set(), set()
        stack = deque()

        row_n = len(grid)
        col_n = len(grid[0])

        for row, row_g in enumerate(grid):
            for col, val in enumerate(row_g):
                if (row, col) not in visited:  
                    stack.append([row, col, -1, -1]) 
                    visited_cur.clear()              
                    while stack:
                        r, c, r_prv, c_prv = stack.pop()
                        if (r, c) in visited_cur:   return True   
                        visited_cur.add((r, c))

                        for d_r, d_c in [[-1, 0], [0, -1], [1, 0], [0, 1]]:
                            if 0 <= r + d_r < row_n   and (r + d_r, c + d_c) != (r_prv, c_prv)  and   \
                               0 <= c + d_c < col_n   and grid[r + d_r][c + d_c] == val:
                                    stack.append([r + d_r, c + d_c, r, c])

                    visited.update(visited_cur) 
        return False
                
            
            
            
            
        
            
        