from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())


def solve():
    x = I()
    n = x.bit_length() - 1
    y = 2 ** n - 1
    
    array = [x, y, x ^ y]
    array.sort()
    # print(array)
    
    if array[0] + array[1] > array[2]:
        print(y)
    else:
        print(-1)
 
 
 
 
T = I()
for _ in range(T):
    solve()