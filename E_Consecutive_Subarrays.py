from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())

def solve():
    n, k = II()
    a = IL()

    prefix = [0]
    for i in a:
        prefix.append(prefix[-1] + i)
    
    prefix = prefix[1:]
    
    print(k * prefix.pop() - sum(sorted(prefix)[:k - 1]))
    
   
 
 
 
T = 1
for _ in range(T):
    solve()