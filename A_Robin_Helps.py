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
    robin = 0
    count = 0
    for i in a:
        if i >= k:
            robin += i 
        elif i == 0:
            if robin:
                robin -= 1
                count += 1

    print(count)

 
 
 
 
T = I()
for _ in range(T):
    solve()