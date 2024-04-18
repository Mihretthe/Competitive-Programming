from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip())

from collections import defaultdict

def solve():
    length = I()
    first = SL()
    gregor = SL()    

    graph = defaultdict(list)

    for i in range(length):
        if gregor[i] == "1":
            if first[i] == "0":
                graph[i].append(i)
            if i > 0 and first[i - 1] == "1":
                graph[i].append(i - 1)
            if i < length - 1 and first[i + 1] == "1":
                graph[i].append(i + 1)

    visited = set()
    for key, value in graph.items():
        for i in value:
            if i not in visited:
                visited.add(i)
                break

    print(len(visited))


 
 
 
 
T = I()
for _ in range(T):
    solve()