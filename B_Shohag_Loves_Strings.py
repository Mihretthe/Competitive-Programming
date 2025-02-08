"""
1 + 2 + 3 + 4

10

1 + 2 + 3 + 4 + 5

5 * 6 / 2

n * (n + 1) / 2 Our formula to calculate the number of substring 

"""

from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())


def solve():
    s = S()

    for i in range(len(s) - 1):
        if s[i] == s[i + 1]:
            print(s[i:i+2])
            return 
        else:
            if i + 2 < len(s):
                if len(set([s[i], s[i + 1], s[i + 2]])) == 3:
                    print(s[i:i + 3])
                    return 
    else:
        print(-1)
 
 
 
T = I()
for _ in range(T):
    solve()