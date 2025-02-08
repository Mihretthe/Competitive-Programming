from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())

from collections import deque, defaultdict
from random import randint

def solve():
    xor = randint(1, 100)
    n = I()
    a = list(map(lambda x : x ^ xor, IL()))
    b = list(map(lambda x : x ^ xor, IL()))

    m = I()
    d = list(map(lambda x : x ^ xor, IL()))

    count = defaultdict(int)

    if a == b:
        if d[-1] in b:
            print("YES")
        else:
            print("NO")
        return

    for i in range(n):
        if a[i] != b[i]:
            count[b[i]] += 1

    b = set(b)
    
    for i in range(m):
        
        if not count:
            if d[-1] in b:
                print("YES")
            else:
                print("NO")
            break

        if d[i] in count:
            count[d[i]] -= 1
            if count[d[i]] == 0:
                del count[d[i]]
        # print(count)
    else:
        if not count:
            print("YES")
        else:
            print("NO")
        




    
            
            
 
 
 
 
T = I()
for _ in range(T):
    solve()
    # print()
    # print()
    # print()