from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())

def calc(num):
    
    answer = []
    
    while num > 0:
        answer.append(str(num % 3))
        num //= 3
    
    return "".join(answer[::-1])

def solve():
    a, c = II()
    
    a3 = (calc(a))
    c3 = (calc(c))
    
    maxi = max(len(a3), len(c3))
    
    a3 = "0" * (maxi - len(a3)) + a3
    c3 = "0" * (maxi - len(c3)) + c3
    
    answer = []
    
    for i in range(len(c3)):
        a = int(a3[i])
        c = int(c3[i])
        
        num = (c - a) % 3
        
        answer.append(num)
    
    # print(answer)
    
    num = 0
    
    for i in range(len(answer)):
        num += (answer[i] * (3**(len(answer) - i - 1)))
    
    print(num)
    
    
 
 
 
T = 1
for _ in range(T):
    solve()