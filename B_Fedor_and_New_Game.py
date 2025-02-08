from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())

def solve():
    n, m, k =II()
    array = []
    for _ in range(m + 1):
        array.append(I())

    count = 0

    fedor = array[-1]
    for i in array[:-1]:
        num = fedor ^ i 
        if num.bit_count() <= k:
            count += 1
    print(count)


 
 
 
 
T = 1
for _ in range(T):
    solve()