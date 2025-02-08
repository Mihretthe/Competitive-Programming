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

    """
    if we have a right we use the prefix 
    else we use the suffix

    0 1 2 3 4 5 6 
     L R R R L L
    
    the problem definition told us that if there is an alternative there is a way 
    

    prefix: 0 1 2 3 3 3
    suffix: 3 2 2 2 2 1
    """

    answer = []

    for i in range(n + 1):
        
        count = 1
        if i == n:
            dxn = s[i - 1]
        else:
            dxn = s[i]
        if dxn == "R":
            for j in range(i + 1, n):
                if dxn != s[j]:
                    count += 1
                    dxn = s[j]
                else:
                    break
        if i > 0 and s[i - 1] == "L":
            dxn = s[i - 1]
            for j in range(i - 1, -1, -1):
                if dxn != s[j]:
                    count += 1
                    dxn = s[j]
                else:
                    break

        answer.append(count)
    
    print(*answer)


 
 
 
T = I()
for _ in range(T):
    solve()