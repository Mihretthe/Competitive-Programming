from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())


def solve():
    n = I()
    ans = []
    a = IL()

    for i in range(n):
        num = i + 1
        count = 1
        index = i 
        while a[index] != num:
            count += 1
            index = a[index] - 1
        ans.append(count)
        
    
    print(*ans)
 
 
 
 
T = I()
for _ in range(T):
    solve()