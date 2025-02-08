from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())

def solve():
    n = I()
    x = IL()
    
    answer = [x[0] + 1]
    for i in range(n - 2):
        pre = answer[-1]
        mini = (x[i + 1] + 1)
        while mini % pre != x[i]:
            mini += 1
        answer.append(mini)
    mini = (answer[-1] + 1)
    while mini % answer[-1] != x[-1]:
        mini += 1
    answer.append(mini)

    print(*answer)


 
 
 
 
T = I()
for _ in range(T):
    solve()