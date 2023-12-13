for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    l = 0
    r = 0
    count = 0

    while r < n:
        flag = True

        while r < n and a[l] == a[r]:
            r += 1
        r -= 1
        if l > 0 and a[l - 1] < a[l]:
            flag = False
        if r < n - 1 and a[r + 1] < a[r]:
            flag = False
        
        if flag:
            count += 1
        
        l = r + 1
        r += 1
    
    if count == 1:
        print("YES")
    else:
        print("NO")

            
         

    
    
        



        