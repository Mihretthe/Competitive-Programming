def I():
    return int(input())

def IL():
    return list(map(int, input().split()))

def S():
    return input()

def NI():
    return map(int, input().split())

def LS():
    return list(input())

def solve(matrix, row, col):
    for r in range(row):
        #Case 1 if the S and T are in the same row
        for c in range(col):
            if matrix[r][c] in "TS":
                i = c - 1
                while i >= 0 and matrix[r][i] == ".":
                    matrix[r][i] = "M"
                    i -= 1
                if i >= 0 and matrix[r][i] in "TS":
                    return True
                i = c + 1
                while i < col and matrix[r][i] == ".":
                    matrix[r][i] = "M"
                    i += 1
                if i < col and matrix[r][i] in "TS":
                    return True
        #check every colum if there is an intersection between the marked 
    for c in range(col):
        r = 0
        while r < row:
            if matrix[r][c] in "TSM":
                r += 1
                while r < row and matrix[r][c] == ".":
                    r += 1
                if r < row and matrix[r][c] in "TSM":
                    return True
            r += 1
    return False
        




    

rows, cols = NI()
matrix = []

for i in range(rows):
    matrix.append(LS())
transponse_matrix = []
for row in zip(*matrix):
    transponse_matrix.append(list(row))

if solve(matrix, rows, cols) or solve(transponse_matrix, cols, rows):
    print("YES")
else:
    print("NO")