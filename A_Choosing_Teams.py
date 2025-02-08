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

    a.sort()

    three = []
    for i in range(0, n, 3):
        if i + 3 <= n:
            three.append(max(a[i:i+3]))
    count = 0
    for i in three:
        if i + k <= 5:
            count += 1
    print(count)

       

 
 
 
 
T = 1
for _ in range(T):
    solve()