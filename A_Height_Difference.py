def I(): return int(input())
 
def II(): return map(int, input().split())
 
def IL(): return list(map(int, input().split()))
 
def SIL(): return sorted(map(int, input().split()),)
 
def solve():
    n, x = II()
    h = SIL()

    first_row = h[:n]
    second_row = h[n:]

    for i in range(n):
        if second_row[i] - first_row[i] < x:
            print("NO")
            break
    else:
        print("YES") 
 
 
 
T = I()
for _ in range(T):
    solve()