from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())

from bisect import bisect_left

def solve():
    n, m, k = II()

    calc = 2 * n * m
    array = []

    for i in range(1, calc + 1, 2 * m):
        array.append(i)

    index = bisect_left(array, k)
    if index < n and k == array[index]:
        if k % 2:
            dxn = "L"
        else:
            dxn = "R"
        print(index + 1, 1, dxn)
        return
    num = array[index - 1]
    if k % 2:
        dxn = "L"
    else:
        dxn = "R"
    row = abs(k - num) // 2 + 1
    print(index, row, dxn)
    
 
 
 
 
T = 1
for _ in range(T):
    solve()