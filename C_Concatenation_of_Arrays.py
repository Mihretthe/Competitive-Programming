from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())


def solve():
    n = I()
    array = []

    for _ in range(n):
        a = IL()
        array.append(tuple(a))
    
    array.sort(key = lambda x : (sum(x), -max(x)))

    concat = []

    for arr in array:
        concat.extend(arr)
    
    print(*concat)

 
 
 
 
T = I()
for _ in range(T):
    solve()