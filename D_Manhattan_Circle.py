from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())

def findcols(row):
    index = row.index("#")
    count = row.count("#")

    return index + count // 2

def solve():
    n, m = II()
    matrix = []

    for _ in range(n):
        matrix.append(S())

    first = last = -1

    rows = []
    
    for i in range(n):
        row = matrix[i]
        if first != -1:
            
            if "#" not in row:
                break     
            rows.append(i)           
            continue

        if "#" not in row:
            continue

        first = i
        last = i
        rows.append(i)
    # print(rows)

    
    mid = len(rows) // 2
    # print(rows[mid])

    print(rows[mid] + 1, findcols(matrix[rows[mid]]) + 1)

        
 
 
 
 
T = I()
for _ in range(T):
    solve()