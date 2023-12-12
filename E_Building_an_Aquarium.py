import math

for _ in range(int(input())):
    n, x = map(int, input().split())
    a = list(map(int, input().split()))

    l = min(a)

    if x == l:
        print(l + 1)
        continue
    if x < l:
        print(l)
        continue
    
    h = math.floor((x + sum(a)) / n)
    print(h)
    




    

    
    

    
