from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())

from bisect import bisect_right


def solve():
    n = I()
    a = IL()
    enum = list(enumerate(a))
    enum.sort(key = lambda x : x[1])
    prefix = 0
    index = 0
    for i in range(n - 1):
        prefix += enum[i][1]
        if prefix < enum[i + 1][1]:
            index = i + 1
    
    print(n - index)
    print(*sorted(map(lambda x: x[0] + 1, enum[index:])))
    




    


 
 
 
 
T = I()
for _ in range(T):
    solve()