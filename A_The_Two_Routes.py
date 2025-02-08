from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())

from collections import defaultdict, deque

def solve():
    n, m = II()
    railways = set()
    flag = False
    

    graph = defaultdict(list)

    for _ in range(m):
        u, v = II()
        
        railways.add((u, v))
        railways.add((v, u))
        if min(u, v) == 1 and max(u, v) == n:
            flag = True
        graph[u].append(v)
        graph[v].append(u)
    if not flag:
        deck = deque([(1, 0)])
        processed = set()

        while deck:
            node, length = deck.popleft()
            if node == n:
                print(length)
                return
            if node in processed:
                continue
            
            for friend in graph[node]:
                if friend not in processed:
                    deck.append((friend, length + 1))

            processed.add(node)
        print(-1)
        return 


    graph = defaultdict(list)
    for i in range(1, n + 1):
        for j in range(i + 1, n + 1):
            if (i, j) not in railways:
                graph[i].append(j)
                graph[j].append(i)
    if not graph:
        print(-1)

        return
    
    deck = deque([(1, 0)])
    processed = set()

    while deck:
        node, length = deck.popleft()
        if node == n:
            print(length)
            return
        if node in processed:
            continue
        
        for friend in graph[node]:
            if friend not in processed:
                deck.append((friend, length + 1))

        processed.add(node)

    

    print(-1)



 
 
 
 
T = 1
for _ in range(T):
    solve()