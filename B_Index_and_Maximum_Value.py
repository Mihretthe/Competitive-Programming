from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())


def solve():
    n, m = II()
    a = IL()
    maxi = max(a)
    answer = []

    for _ in range(m):
        c, l, r = SL()
        l, r = int(l), int(r)
        if l <= maxi <= r:
            if c == "+":
                maxi += 1
            else:
                maxi -= 1
        answer.append(maxi)

    print(*answer)


 
 
 
 
T = I()
for _ in range(T):
    solve()