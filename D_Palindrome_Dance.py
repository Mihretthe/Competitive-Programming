from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())


def solve():
    n, white, black = II()
    a = IL()
    left = 0
    right = n - 1
    cost = 0

    while left <= right:
        if (a[left] == 0 and a[right] == 1) or (a[left] == 1 and a[right] == 0):
            print(-1)
            return
        else:
            if a[left] == 2:
                if a[right] == 1:
                    cost += black
                elif a[right] == 0:
                    cost += white
                else:
                    if left == right:
                        cost += (min(black, white))
                    else:
                        cost += (min(black, white) * 2)
            elif a[right] == 2:
                if a[left] == 1:
                    cost += black
                else:
                    cost += white
            
            
            left += 1
            right -= 1
    
    print(cost)

 
 
 
 
T = 1
for _ in range(T):
    solve()