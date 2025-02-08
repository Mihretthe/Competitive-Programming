from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())

def solve():
    s = S()
    opens = 0
    array = []
    n = len(s)
    for i in range(n):
        array.append((opens, -i, s[i]))
        if s[i] == "(":
            opens += 1
        else:
            opens -= 1

    
    array.sort()

    print("".join(list(map(lambda x : x[2], array))))


 
 
 
 
T = 1
for _ in range(T):
    solve()