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
    indegree = defaultdict(int)
    elements = set()
    pre = None
    flag = False
    for _ in range(n):
        new_str = S()
        if not pre:
            pre = new_str            
        else:

            for i in range(min(len(pre), len(new_str))):                
                if pre[i] == new_str[i]:
                    # print(pre, new_str)
                    continue
                else:
                    elements.add(pre[i])
                    elements.add(new_str[i])
                    graph[pre[i]].append(new_str[i])
                    indegree[new_str[i]] += 1
                    pre = new_str
                    break
            else:
                if len(new_str) > len(pre):
                    elements.add(new_str[len(pre) - 1])
                elif len(pre) > len(new_str):                    
                    flag = True
      
            pre = new_str
    if flag:
        print("Impossible")
        return
            
    print(graph)
    
    deck = deque()
    
    for i in elements:
        if i not in indegree:
            deck.append(i)
    
    
    answer = deck.copy()
   
    while deck:
        node = deck.popleft()

        for i in graph[node]:
            indegree[i] -= 1
            if indegree[i] == 0:
                deck.append(i)
                answer.append(i)

    # print(answer, elements)
    if len(answer) == len(elements):
        
        for i in "abcdefghijklmnopqrstuvwxyz":
            if i not in answer:
                answer.append(i)
        print("".join(answer))
    else:
        print("Impossible")
        


 
 
 
 
T = 1
for _ in range(T):
    solve()