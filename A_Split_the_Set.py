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

    even = 0
    odd = 0

    for num in a:
        if num % 2:
            odd += 1
        else:
            even += 1
    
    if even == odd:
        print("Yes")
    else:
        print("No")


 
 
 
 
T = I()
for _ in range(T):
    solve()