from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())

from collections import defaultdict, deque

def solve():
    n = I()
    graph = defaultdict(list)
    respect = [0]
    for i in range(1, n + 1):
        p, c = II()
        if p != -1:
            graph[p].append(i)
        respect.append(c)

    
    answer = []

    for i in range(1, n + 1):
        if respect[i] == 1:
            for child in graph[i]:
                if respect[child] == 0:                   
                    break
            else:
                answer.append(i)
    
    

    if answer:
        print(*sorted(answer))
    else:
        print(-1)
        




 
 
 
 
T = 1
for _ in range(T):
    solve()