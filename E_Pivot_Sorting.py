import math


"""
middle
"""
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    x = 0

    for i in range(n - 1):
        if a[i + 1] < a[i]:
            x = max(x,(math.ceil((a[i + 1] + a[i]) / 2))) 
            

    for i in range(n):
        a[i] = abs(a[i] - x)
    
    if a == sorted(a):
        print(x)
    else:
        print(-1)
    

    
        
    


    
    

    


        