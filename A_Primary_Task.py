from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())


def solve():
    a = S()
    if len(a) < 3:
        print("NO")
        return
    
    if a[:2] != "10":
        print("NO")
        return
    
    if a[2] == "0" or int(a[2:]) < 2:
        print("NO")
        return

    print("YES")
 
 
 
 
T = I()
for _ in range(T):
    solve()