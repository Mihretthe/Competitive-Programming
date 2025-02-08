from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())

def solve():
    n = I()
    p = IL()
    count = 0

    for i in range(n):
        for j in range(i + 1, n):
            if (p[i] * p[j]) % ((i + 1) * (j + 1)) == 0:
                count += 1

    print(count)
 
 
 
 
T = I()
for _ in range(T):
    solve()