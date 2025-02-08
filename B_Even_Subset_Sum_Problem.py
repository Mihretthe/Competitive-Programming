from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())


def solve():
    n = I()
    a = IL()
    
    odd = False
    
    for i in range(n):
        if a[i] % 2 == 0:
            print(1)
            print(i + 1)
            break
        else:
            if odd:
                print(2)
                print(odd, i + 1)
                break
            else:
                odd = i + 1
    else:
        print(-1)                
    
 
 
 
 
T = I()
for _ in range(T):
    solve()