
def I(): return int(input())
 
def II(): return map(int, input().split())
 
def IL(): return list(map(int, input().split()))
 
def SIL(): return sorted(map(int, input().split()),)


def solve():
    n = I()
    a = IL()
    

    for i in range(1,n - 1):
        if a[i] == 0:
            continue
        if a[i - 1] * 2 > a[i] or a[i + 1] < a[i - 1]:
            print("NO")
            break
        else:
            a[i] -= (a[i - 1] * 2)
            a[i + 1] -= a[i - 1]
            a[i - 1] = 0        
    else:
        if set(a) == {0}:
            print("YES")
        else:
            print("NO")

T = I()
for _ in range(T):
    solve()