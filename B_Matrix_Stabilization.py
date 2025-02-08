from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())

def solve():
    n, m = II()

    matrix = []

    for _ in range(n):
        matrix.append(IL())
    
    directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]

    def inbound(row, col):
        return 0 <= row < n and 0 <= col < m

    for i in range(n):
        for j in range(m):

            maxi = 0
            count = 0
            inbou = 0

            for r, c in directions:
                newr = r + i 
                newc = c + j

                if inbound(newr, newc):
                    inbou += 1
                    if matrix[i][j] > matrix[newr][newc]:
                        count += 1
                    maxi = max(maxi, matrix[newr][newc]) 

            if count == inbou:
                matrix[i][j] = maxi


    for i in range(n):
        print(*matrix[i])
 
 
 
 
T = I()
for _ in range(T):
    solve()