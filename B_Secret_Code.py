from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())

def calc(n):
    if n % 2:
        return n // 2
    return n // 2 - 1

def solve():
    n = I()
    s = S()
    answer = [""] * n
    start = 0
    for i in range(n - 1, -1, -2):
        left, right = s[i - 1], s[i]
        answer[start] = left
        answer[n - start - 1] = right
        start += 1

    print("".join(answer))





    
 
 
 
 
T = 1
for _ in range(T):
    solve()