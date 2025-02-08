from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())


def solve():
    n, h = II()

    a = IL()
    count = 0
    for i in a:
        if i > h:
            count += 2
        else:
            count += 1
    
    print(count)
 
 
 
 
T = 1
for _ in range(T):
    solve()