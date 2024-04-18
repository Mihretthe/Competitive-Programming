def I(): return int(input())
 
def II(): return map(int, input().split())
 
def IL(): return list(map(int, input().split()))
 
def SIL(): return sorted(map(int, input().split()),)


def solve():
    n, h = II()
    a = list()

    for i in range(n):
        a.append(max(IL()))
    

    a.sort(reverse = True)
    pre = 0
    for i in a:
        pre += i
        if pre >= h:
            print("YES")
            break
    else:
        print("NO")
    
    
 
T = I()
for _ in range(T):
    solve()