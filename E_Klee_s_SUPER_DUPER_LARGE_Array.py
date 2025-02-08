from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())

def solve():
    n,k = II()
    
    #n*[a1 + an]//2
    n=(k+n-1)

    pre = ((k-1)*(k))//2
    all = (n*(n+1))//2

    def check(num):
        left = ((num*(num + 1))//2 ) - pre
        right = all - ((num*(num + 1))//2 )

        
        return left,right
    

    l = k-1
    r = n

    while l+1 < r:
        mid = (l+r)//2

        
        left,right = check(mid)
        print(left , right)
        if left > right:
            r = mid
        else:
            l = mid

    print(r , "here")
    print(r-k+1)

 
T = int(input())
for _ in range(T):
    solve()