from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())


def solve():
    a = I()
    b = I()

    mid = (a + b) // 2

    for_a = abs(a - mid)
    for_b = abs(b - mid)

    answer = (for_a * (for_a + 1)) // 2 + (for_b * (for_b + 1)) // 2

    print(answer)
 
 
 
 
T = 1
for _ in range(T):
    solve()