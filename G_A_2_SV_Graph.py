from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())


def solve():
    s = S()

    if s == "A":
        print("5 5")
        print("5 2")
        print("3 1")
        print("4 2")
        print("1 4")
        print("1 2")
    elif s == "2":
        print(4,3)
        print(1, 2)
        print(2, 3)
        print(3, 4)
    elif s == "S":
        print(4, 3)
        print(1, 2)
        print(2, 3)
        print(3, 4)
    elif s == "V":
        print(3, 2)
        print(1,2)
        print(2, 3)

 
 
 
 
T = 1
for _ in range(T):
    solve()