from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())


def solve():
    n, a, b = II()
    s = S()

    x = 0
    y = 0

    s = s * 2000

    horizontal = []
    vertical = []

    for i in s:
        if i == "N":
            vertical.append(1)
            horizontal.append(0)
        elif i == "S":
            vertical.append(-1)
            horizontal.append(0)
        elif i == "E":
            vertical.append(0)
            horizontal.append(1)
        else:
            vertical.append(0)
            horizontal.append(-1)
    
   
    for i in range(1, len(s)):
        horizontal[i] += horizontal[i - 1]
        vertical[i] += vertical[i - 1]

    for i in range(len(s)):
        if horizontal[i] == a and vertical[i] == b:
            print("YES")
            break
    else:
        print("NO")
 
 
 
 
T = I()
for _ in range(T):
    solve()