from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())


def solve():
    n = I()
    matrix = []
    not_one = []
    ans = []
    for i in range(n):
        row = IL()
        matrix.append(row)
        for j in range(n):
            if row[j] != 1:
                not_one.append((i, j))


    count = 0
    for x, y in not_one:
        row = matrix[x]
        row = row[:y] + row[y + 1:]
        col = []

        for i in range(n):
            if i == x:
                continue
            col.append(matrix[i][y])
        
        
        flag = False
        for a in row:
            for b in col:
                if a + b == matrix[x][y]:
                    count += 1
                    flag = True
                    break
            if flag:
                break
            
    if count == len(not_one):
        print("Yes")
    else:
        print("No")
    








 
 
 
 
T = 1
for _ in range(T):
    solve()