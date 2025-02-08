from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())


def solve():
    num = S()
    if "0" not in num:
        print("cyan")
        return
    
    num = list(num)
    num.remove("0")

    tot = 0
    even = False

    for i in num:
        n = int(i) 
        tot += n
        if n % 2 == 0:
            even = True

    if even and tot % 3 == 0:
        print("red")
    else:
        print("cyan")


 
 
 
 
T = I()
for _ in range(T):
    solve()