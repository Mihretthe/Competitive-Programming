from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())


def solve():
    n = I()
    answer = 0

    if n:
        answer += n // 5
        n %= 5

    if n:
        answer += n // 4
        n %= 4
    
    if n:
        answer += n // 3
        n %= 3

    if n:
        answer += n // 2
        n %= 2
    
    if n:
        answer += 1

    print(answer)
 
 
 
 
T = 1
for _ in range(T):
    solve()