def I(): return int(input())
 
def II(): return map(int, input().split())
 
def IL(): return list(map(int, input().split()))
 
def SIL(): return sorted(map(int, input().split()),)

def S() : return input()
 
def solve():
    a, b = S().split()

    ans = a[0]

    i = 1
    j = 0

    while i < len(a):
        if a[i] >= b[j]:
            ans += b[j]
            break
        else:
            ans += a[i]
            i += 1
    else:
        ans += b[j]

    print(ans)




 
 
 
 
T = 1
for _ in range(T):
    solve()