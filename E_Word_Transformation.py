from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())

from collections import Counter, deque, defaultdict

def solve():
    s, t = S().split()
    n = len(s)
    sc = Counter(s)
    tc = Counter(t)
    indices = defaultdict(deque)

    
    for key, value in tc.items():
        if key not in sc or value > sc[key]:
            print("NO")
            return 
    stack = []
    index = 0
    for i in s:
        if tc[i] == sc[i]:
            if index < len(t) and t[index] == i:
                stack.append(i)
                index += 1
                tc[i] -= 1
            
        sc[i] -= 1
        
            
    
    if "".join(stack) != t:
        print("NO")
    else:
        print("YES")

        
        
            

    

    
    

    
 
 
 
T = I()
for _ in range(T):
    # print(_)
    solve()