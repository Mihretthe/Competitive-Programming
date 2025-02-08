from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())




def solve():
    u, v = II()
    if u in {1, 2, 3, 4} and v in {1, 2, 3, 4}:
        print("Yes")
    elif u in {5, 6, 7} and v in {5, 6, 7}:
        print("Yes")
    elif u in {8, 9} and v in {8, 9}:
        print("Yes")
    else:
        print("No")

    
 
 
 
 
T = I()
for _ in range(T):
    solve()