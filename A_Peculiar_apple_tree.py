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
    a = IL()

    graph = defaultdict(list)
    parent = {}
    

    for i in range(len(a)):
        graph[a[i]].append(i + 2)

    deck = deque([(1, 0)])

    counter = defaultdict(int)

    while deck:
        node, length = deck.popleft()

        for friend in graph[node]:
            deck.append((friend, length + 1))
        
        counter[length] += 1
    
    answer = 0
    for key, val in counter.items():
        answer += val % 2

    print(answer)

    
    
    


 
 
 
 
T = 1
for _ in range(T):
    solve()