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

    indices = {}

    for i in range(n):
        if a[i] not in indices:
            indices[a[i]] = i
    
    if len(indices) < k:
        print("NO")
        return 
    answer = []
    for key, value in indices.items():
        if not k:
            break
        answer.append(value + 1)
        k -= 1
    
    print("YES")
    print(*answer)
 
 
 
 
T = 1
for _ in range(T):
    solve()