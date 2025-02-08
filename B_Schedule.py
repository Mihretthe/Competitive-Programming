from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())


def solve():
    n = I()
    a = IL()
    stay = False
    count = 0
    for i in range(n):
        if stay:
            if a[i] == 0:
                if i == n - 1:
                    continue
                else:
                    if a[i + 1] == 0:
                        stay = False
                    else:
                        count += 1
            else:
                count += 1
        else:
            if a[i] == 0:
                continue
            else:
                stay = True
                count += 1

    print(count)





 
 
 
 
T = 1
for _ in range(T):
    solve()