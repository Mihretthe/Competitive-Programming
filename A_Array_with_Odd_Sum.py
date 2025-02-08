from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())

def check(a):
    even = 0
    odd = 0

    for i in a:
        if i % 2:
            odd += 1
        else:
            even += 1
    return (even, odd)

def solve():
    n = I()
    a = IL()

    even, odd = check(a)

    if even and odd:
        print("YES")
    elif odd:
        if n % 2:
            print("YES")
        else:
            print("NO")
    elif even:
        print("NO")

 
 
 
 
T = I()
for _ in range(T):
    solve()