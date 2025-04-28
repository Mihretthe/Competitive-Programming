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
    r = IL()
    
    graph = defaultdict(list)
    indegree = defaultdict(int)
    
    for i in range(n):
        graph[i + 1].append(r[i])
        indegree[r[i]] += 1 
        
    
    previous = [1] * (n + 1)
    
    deck = deque()
    
    for i in range(1, n + 1):
        if not indegree[i]:
            deck.append(i)
    
    count = 2
    while deck:
        count += 1
        for _ in range(len(deck)):
            node = deck.popleft()
            previous[node] = 0
            for neigh in graph[node]:
                indegree[neigh] -= 1
                if indegree[neigh] == 0:
                    deck.append(neigh)
                    
            
    
    print(count)
    
    
    
 
 
 
 
T = I()
for _ in range(T):
    solve()