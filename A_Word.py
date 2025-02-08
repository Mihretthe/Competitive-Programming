from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())


def solve():
    s = S()

    uppers = 0
    lowers = 0

    for i in s:
        if ord(i) >= 97:
            lowers += 1
        else:
            uppers += 1

    if uppers <= lowers:
        print(s.lower())
    else:
        print(s.upper())
 
 
 
 
T = 1
for _ in range(T):
    solve()