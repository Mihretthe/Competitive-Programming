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

    a.sort(reverse= True)

    al = True
    alice = 0
    bob = 0

    for i in range(n):
        if al:
            alice += a[i]
        else:
            if k > 0:
                bob += a[i] + min(k, a[i - 1] - a[i])
                k -= min(k, a[i - 1] - a[i])
            else:
                bob += a[i]
            

        al = not al
    
    print(alice - bob)
            
    
    

    
    

 
 
 
T = I()
for _ in range(T):
    solve()