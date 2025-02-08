from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())

array = [0]

for i in range(1, 100000):
    array.append(array[-1] + i)

from bisect import bisect_right


def solve():
    l, r = II()
    ans = bisect_right(array, r - l)
    print(ans)
 
 
 
 
T = I()
for _ in range(T):
    solve()