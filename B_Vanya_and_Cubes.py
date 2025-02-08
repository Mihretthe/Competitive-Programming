from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())

from bisect import bisect_right

array = [1]
for i in range(2, 10001):
    array.append(array[-1] + i)

for i in range(1, 10000):
    array[i] += array[i - 1]


def solve():
    n = I()
    print(bisect_right(array, n))
 
 
 
 
T = 1
for _ in range(T):
    solve()