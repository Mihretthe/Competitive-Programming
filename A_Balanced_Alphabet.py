from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())

def solve():
    n, k = II()
    letters = "abcdefghijklmnopqrstuvwxyz"

    answer = []

    for i in range(k):
        answer.append(letters[i] * (n//k))
    
    answer = ''.join(answer)
    if len(answer) < n:
        answer += answer[-1] * (n - len(answer))
    
    print(answer)

 
 
 
 
T = I()
for _ in range(T):
    solve()