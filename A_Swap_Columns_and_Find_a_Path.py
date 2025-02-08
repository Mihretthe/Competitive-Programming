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
    b = IL()

    array = []

    for i in range(n):
        array.append((a[i], b[i]))
    
    array.sort()

    print(array)

    2 8 5 3 
    1 10 3 4

    2 5 8 3
    1 3 10 4

    1  2   3
    10 -5  -3
 
    2 3 1
    -5 -3 10
 
T = I()
for _ in range(T):
    solve()