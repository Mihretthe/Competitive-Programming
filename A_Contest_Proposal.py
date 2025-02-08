from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())

def solve():
    n = I()
    array = IL()
    brray = IL()
    count = 0

    i = 0
    j = 0
    while  j < n:
        if array[i] <= brray[j]:
            i += 1
            j += 1
        else:
            count += 1
            j += 1
    
    print(count)
        


 
 
 
 
T = I()
for _ in range(T):
    solve()