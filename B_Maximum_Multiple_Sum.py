from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())

def solve():
    n = I()
    calc = 2
    answer = 2

    for x in range(2, n + 1):
        
        ans = 0
        for i in range(1, n + 1):            
            if i * x > n:
                break
            ans += i * x
        if ans >= calc:
            calc = ans
            answer = x
            
    print(answer)
            



        


 
 
 
 
T = I()
for _ in range(T):
    solve()