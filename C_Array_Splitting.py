from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())


def solve():
    n, k = II()
    a = IL()
    collect = []
    for i in range(1, n):
        collect.append(a[i] - a[i - 1])
    
    collect.sort()
    
    print(sum(collect[:n - k]))
 
 
 
 
T = 1
for _ in range(T):
    solve()