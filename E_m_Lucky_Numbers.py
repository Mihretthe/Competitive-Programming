for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    ans = []
    
    for i in range(1, n + 1):
        b = set(a[:i])
        j = 0
        r = i
        while r < n + 1:
            s = set(a[j:r])
            b = s.intersection(b)
            j += 1
            r += 1
        if b:
            ans.append(min(b))
        else:
            ans.append(-1)
                 
        
    print(*ans)