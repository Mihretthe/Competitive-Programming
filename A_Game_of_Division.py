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

    for i in range(n):
        count = 0
        for j in range(n):
            if i == j:
                continue
            if abs(a[i] - a[j]) % k:
                count += 1
        if count == n - 1:
            print("YES")
            print(i + 1)
            return
    print("NO")

 
 
 
 
T = I()
for _ in range(T):
    solve()