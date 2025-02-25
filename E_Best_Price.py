from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())


def solve():
    n, k = II()
    
    a = IL()
    b = IL()
    
    array = []
    
    for i in range(n):
        array.append((a[i],0))
        array.append((b[i],1))
    
    array.sort()
    
    zeros = [0]
    ones = [0]
    print(array)
    
    for i in range(2 * n):
        if array[i][1] == 0:
            zeros.append(zeros[-1] + 1)
            ones.append(ones[-1])
        else:
            ones.append(ones[-1] + 1)
            zeros.append(zeros[-1])
    
    print(zeros)
    print(ones)
    
 
 
 
 
T = I()
for _ in range(T):
    solve()