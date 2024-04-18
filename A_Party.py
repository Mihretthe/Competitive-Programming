from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())
from collections import defaultdict

def solve():
    length = I()
    employee = []
    counter = defaultdict(list)

    for _ in range(length):
        num = I()
        employee.append(num)
        counter[num].append(_ + 1)

  
    visited = set([1])
    stack = [1]
    count = 0
    while stack:
        
        node = stack.pop()
        
        for i in counter[node]:
            if i not in visited:
                count += 1
                stack.append(i)
                visited.add(i)

    print(count)


    



 
 
 
 
T = 1
for _ in range(T):
    solve()