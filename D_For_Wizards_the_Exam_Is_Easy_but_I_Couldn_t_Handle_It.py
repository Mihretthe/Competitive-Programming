from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())


def solve():
    n = I()
    a = IL()
    
    array = [0 for _ in range(n)]
    
    for i in range(n):
        for j in range(i + 1, n):
            if a[i] > a[j]:
                array[i] += 1
    # print(array)
    ans = []
    total = sum(array)
    mini = total
    for i in range(n):
        tot = total
        if not array[i]:
            continue
        for j in range(i + 1, n):
            if a[i] < a[j]:
                tot += 1
            elif a[i] > a[j]:
                tot -= 1
            if tot < mini:
                ans = [i + 1, j + 1]
            # print(a[i], a[j],tot, mini)
            mini = min(tot, mini)     
    if ans:
        print(*ans)
    else:
        print(1, 1)
            
 
 
 
 
T = I()
for _ in range(T):
    # print(_)
    solve()