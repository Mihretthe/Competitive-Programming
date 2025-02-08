from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())

def solve():
    n, k, b, s = II()
    p = IL()
    a = IL()
    k2 = k

    array = [0] * (n + 1)
    for i in range(n):
        array[p[i]] = a[i]

    
    
   

    #Bodya

    b -= 1
    s -= 1
    running = 0
    current = 0
    running2 = 0
    current2 = 0
    set_b = set()
    set_s = set()
    while k > 0:  
        if b in set_b:
            break      
        current = max(current, running + (a[b])* (k ))
        running += a[b]
        set_b.add(b)
        if b == p[b] - 1:
            break
        b = p[b] - 1
        k -= 1
    
    
    while k2 > 0: 
        if s in set_s:
            break
        set_s.add(s)
        current2 = max(current2, running2 + (a[s])* k2)
        running2 += a[s]
        if s == p[s] - 1:
            break
        s = p[s] - 1
        k2 -= 1

    
    if current > current2:
        print("Bodya")
    elif current2 > current:
        print("Sasha")
    else:
        print("Draw")
    


 
 
 
 
T = I()
for _ in range(T):
    solve()