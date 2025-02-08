from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())


def solve():
    n, m, till = II()
    count = 0

    for i in range(1, till + 1):
        if i % n == 0 and i % m == 0:
            count += 1
    
    print(count)

print(100000000 // 7)
 
 
 
 
T = 1
for _ in range(T):
    solve()