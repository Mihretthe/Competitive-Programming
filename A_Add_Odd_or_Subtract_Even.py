from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())

def solve():
    n, m = II()
    count = 0
    for i in range(n + 1):
        for j in range(m + 1):
            if i*i + j == n and j * j + i == m:
                count += 1

    print(count)
 
 
 
T = I()
for _ in range(T):
    solve()