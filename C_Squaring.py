from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())


def solve():
    n = I()
    a = IL()
    count = 0

    for i in range(1, n):
        if a[i] < a[i - 1]:
            if a[i] == 1:
                print(-1)
                return
            while a[i] < a[i - 1]:
                a[i] *= a[i]
                count += 1
    print(count)
 
 
 
 
T = I()
for _ in range(T):
    solve()