from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())


def solve():
    n = I()
    
    fibonaccis = [1, 1]
    
    for i in range(2, n + 1):
        fibonaccis.append(fibonaccis[i - 2] + fibonaccis[i - 1])
        
    
    fibonaccis = set(fibonaccis)
    answer = []
    for  i in range(1, n + 1):
        if i in fibonaccis:
            answer.append("O")
        else:
            answer.append("o")
    
    print("".join(answer))
    
 
 
 
 
T = 1
for _ in range(T):
    solve()