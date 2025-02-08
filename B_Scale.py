from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())


def solve():
    n, k = II()
    matrix = []

    for _ in range(n):
        row =list( map(int,list(input())))
        matrix.append(row)
    # print(matrix)
    ans = []
    for i in range(0,n,k):
        row = []
        for j in range(0,n,k):
            row.append(str(matrix[i][j]))
        ans.append(row)
    # print(ans)
    
    for i in range(n//k):
        print("".join(ans[i]))


 
 
 
T = I()
for _ in range(T):
    solve()