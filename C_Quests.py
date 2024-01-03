for _ in range(int(input())):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = k - n
   
    max_experience = a[0]
    tracker = b[0]
    
    i = 1
    while k > 1 and i < n:
        if tracker > a[i]:
            max_experience += tracker
        else:
            max_experience += a[i]
            tracker = max(b[i], tracker)
            i += 1      
        k -= 1
    
    if c > 0:
        max_experience += (c * tracker)
        
    print(max_experience)
            
        

    

