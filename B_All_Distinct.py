def I(): return int(input())
 
def II(): return map(int, input().split())
 
def IL(): return list(map(int, input().split()))
 
def SIL(): return sorted(map(int, input().split()),)

from collections import Counter, defaultdict
 
def solve():
    n = I()
    a = IL()
    counter = Counter(a)
    x = len(counter)

    if x % 2 == n % 2:
        print(x)
    else:
        print(x - 1)
        
T = I()
for _ in range(T):
    solve()