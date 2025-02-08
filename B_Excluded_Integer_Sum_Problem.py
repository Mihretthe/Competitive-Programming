from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())

def solve():


    n, k, x = II()
    
    if x != 1:
        print("YES")
        print(n)
        ans = [1] * n
        print(*ans)
    elif k == 1 or (k == 2 and n % 2):
        print("NO")
    else:
        print("YES")
        ans = []
        if n % 2:
            ans.append(3)
        else:
            ans.append(2)

        ans += [2] * ((n // 2) - 1)
        print(n // 2)
        print(*ans)
        



    
        





 
 
 
 
T = I()
for _ in range(T):
    solve()