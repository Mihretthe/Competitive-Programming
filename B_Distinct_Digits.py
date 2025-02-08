from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())

def solve():
    n = I()
    num = 9
    if n < 10:
        print(n)
        return
    
    ans = []
    while n > 0:
        ans.append(str(num))
        n -= num
        num -= 1
       

    
    ans[-1] = str(int(ans[-1]) + n)

    print("".join(ans[::-1]))

 
 
 
 
T = I()
for _ in range(T):
    solve()