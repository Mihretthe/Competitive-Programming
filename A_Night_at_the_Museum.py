from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())


letters = "abcdefghijklmnopqrstuvwxyz"

def calc(curr, to):
    curr = letters.index(curr) + 1
    to = letters.index(to) + 1
    # print(curr, to)
    return min((26 - abs(curr - to)), abs(to - curr))

def solve():
    s = S()

    start = "a"
    ans = 0
    for i in s:
        ans += calc(start, i)
        start = i 
        # print(ans)

    print(ans)



 
 
 
 
T = 1
for _ in range(T):
    solve()