from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())

def solve():
    n, m = II()
    s = list(S())
    # ind = sorted(list(set(IL())))
    ind = sorted(IL())
    new_ind = []
    c = sorted(S())[::-1]

    for i in ind:
        if new_ind and i == new_ind[-1]:
            continue
        new_ind.append(i)
    
    for i in new_ind:
        s[i - 1] = c.pop()

    print("".join(s))

    
    






 
 
 
 
T = I()
for _ in range(T):
    solve()