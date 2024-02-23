from collections import deque

for _ in range(int(input())):
    n = int(input())
    s = input()
    sheeps = 0
    prefix = [0] * n
    suffix = [0] * n
    no_sheeps = 0

    for i in range(n - 1, -1, -1):
        if s[i] == ".":
            suffix[i] += no_sheeps
        else:
            no_sheeps += 1
    
            
    no_sheeps = 0
    for i in range(n):
        if s[i] == ".":
            prefix[i] += no_sheeps
        else:
            no_sheeps += 1
    
    for i in range(1,n):
        prefix[i] += prefix[i - 1]
   
    for i in range(n - 1, 0, -1):
        suffix[i - 1] += suffix[i]
        
    min_operation = float('inf')
    for i, j in zip(prefix, suffix):
        min_operation = min(min_operation, i + j)
    
    print(min_operation)



