from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())

from collections import defaultdict

def solve():
    n, q = II()
    ways = SL()
    graph = defaultdict(list)
    graph2 = defaultdict(list)

    for i in range(n):
        graph[ways[i][0]].append(i + 1)
        graph[ways[i][1]].append(i + 1)
        # graph2[i + 1].append(ways[i][0])
        # graph2[i + 1].append(ways[i][1])    
    print(graph)

    def backtrack(index):
        pass
    
    for _ in range(q):
        start, end = II()
        way_s = ways[start - 1]
        way_e = ways[end - 1]
        print(way_s, way_e)
        if way_s[0] == way_e[0] or way_s[1] == way_e[1]:
            print("YES")
        else:
            print("NO")
             

 
 
 
 
T = I()
for _ in range(T):
    solve()