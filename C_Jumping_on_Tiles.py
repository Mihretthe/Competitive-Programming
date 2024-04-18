from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())

def solve():
    letters = "abcdefghijklmnopqrstuvwxyz"
    s = S()
    first = letters.index(s[0])
    last = letters.index(s[-1])
    print(abs(first - last), 2)
    print(1, len(s))

 
 
 
T = I()
for _ in range(T):
    solve()