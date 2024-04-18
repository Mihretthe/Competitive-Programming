def I(): return int(input())
 
def II(): return map(int, input().split())
 
def IL(): return list(map(int, input().split()))
 
def SIL(): return sorted(map(int, input().split()),)
 
def solve():
    n = I()
    flag = False
    mini = 0
    maxi = float('inf')
    not_equal = set()

    for _ in range(n):
        a, x = II()
        
        if not flag:
            if a == 1:
                mini = max(mini, x)
            elif a == 2:
                maxi = min(maxi, x)
            else:
                not_equal.add(x)
            
            if maxi < mini:
                print(0)
                flag = True
    
    if not flag:
        ans = (maxi - mini + 1)
        
        for i in not_equal:
            if i >= mini and i <= maxi:
                ans -= 1
        
        print(ans)
 
 
 
 
T = I()
for _ in range(T):
    solve() 