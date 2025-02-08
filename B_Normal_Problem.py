from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())


def solve():
    s = S()
    ans = []

    for i in s:
        if i == "p":
            ans.append("q")
        elif i == "q":
            ans.append("p")
        else:
            ans.append(i)
    
    print("".join(ans[::-1]))
 
 
 
 
T = I()
for _ in range(T):
    solve()