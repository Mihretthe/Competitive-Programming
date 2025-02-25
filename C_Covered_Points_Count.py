from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())

from collections import defaultdict

# Line swip using dictionary

def solve():
    n = I()
    line = defaultdict(int)
    
    for _ in range(n):
        l, r = II()
        line[l] += 1
        line[r + 1] -= 1
    
    keys = list(line.keys())
    keys.sort()
    
    answer = defaultdict(int)
    for i in range(1, len(keys)):
        line[keys[i]] += line[keys[i - 1]]
        

    for i in range(1, len(keys)):
        calc = line[keys[i - 1]]        
        answer[calc] += keys[i] - keys[i - 1]
        
    ans = []
    for i in range(1, n + 1):
        ans.append(answer[i])
    
    print(*ans)
             
        
        
 
 
 
 
T = 1
for _ in range(T):
    solve()