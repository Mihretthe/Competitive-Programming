from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())


def solve():
    n = I()
    s = S()

    a = s[0]
    if a == "0":
        first = True
    else:
        first = False
    
    count = 0

    for i in range(n):
        if first:
            if s[i] == "1":
                a = "1"
                first = False
            continue
        if s[i] != a:
            a = s[i]
            count += 1

    print(count)
                
        
            

 
 
 
 
T = I()
for _ in range(T):
    solve()