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
    count = 0
    total = 0

    maxi = 0

    for i in a:
        maxi = max(i, maxi)
        total += i
        if maxi == total - maxi:
            count += 1
        

    print(count)

    

 
 
 
 
T = I()
for _ in range(T):
    solve()