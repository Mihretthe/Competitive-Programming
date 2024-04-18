
def I(): return int(input())
 
def II(): return map(int, input().split())
 
def IL(): return list(map(int, input().split()))
 
def SIL(): return sorted(map(int, input().split()),)
 
def solve():
    n, m, k = II()
    b = IL()
    c = IL()

    b.sort()
    c.sort()

    count = 0

    for i in b:
        for j in c:
            if i + j <= k:
                count += 1
    
    print(count)

 
 
 
 
T = I()
for _ in range(T):
    solve()