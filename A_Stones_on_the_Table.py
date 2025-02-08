from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())


def solve():
    stack = []
    n = I()
    s = S()

    for i in s:
        if stack and stack[-1] == i:
            continue
        stack.append(i)
    
    print(n - len(stack))
 
 
T = 1
for _ in range(T):
    solve()