from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())


def solve():
    n = I()
    substrings = []

    for _ in range(n):
        s = S()
        substrings.append(s)

    substrings.sort(key = lambda x : len(x))

    for i in range(1, n):
        if substrings[i - 1] not in substrings[i]:
            print("NO")
            break
    else:
        print("YES")
        for i in substrings:
            print(i)
 
 
 
 
T = 1
for _ in range(T):
    solve()