from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())


    

def solve():
    s = S()
   

    n = len(s)
    carry = 0

    for i in range(n - 1, -1, -1):
        need = int(s[i]) - carry
        carry = 1
        if need < 0 or need == 9:
            print("NO")
            return
        
    if need == 0:
        print("YES")
    else:
        print("NO")


 
 
 
 
T = I()
for _ in range(T):
    solve()