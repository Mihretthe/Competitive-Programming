from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())

from collections import defaultdict




def solve():
    n = I()
    hashmap = defaultdict(int)
    for _ in range(n):
        command = IL()
        if len(command) == 4:
            comm, u, v, w = command
            while u != v:
                if u > v:
                    res = u // 2
                    hashmap[(res, u)] += w
                    u = res
                else:
                    res = v // 2
                    hashmap[(res, v)] += w
                    v = res
        else:
            comm, u, v = command
            ans = 0
            while u != v:
                if u > v:
                    res = u // 2
                    ans += hashmap[(res, u)]
                    u = res
                else:
                    res = v // 2
                    ans += hashmap[(res, v)]
                    v = res

            print(ans)
         
 
 
 
 
T = 1
for _ in range(T):
    solve()