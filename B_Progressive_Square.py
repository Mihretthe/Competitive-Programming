from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())

def solve():
    n, c, d = II()
    a = IL()

    mini = min(a)
    row = []
    for i in range(n):
        if row:
            row.append(row[-1] + d)
        else:
            row.append(mini)
    for i in range(n - 1):
        roww = row[-n:]
        for i in range(n):
            row.append(roww[i] + c)
    row.sort()
    a.sort()
    if row == a:
        print("YES")
    else:
        print("NO")
 
 
 
T = I()
for _ in range(T):
    solve()