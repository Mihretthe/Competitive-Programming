for _ in range(int(input())):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    h = list(map(int, input().split()))
    ans = 0

    i = 0

    while i < n - 1:
        start = i
        while i < n - 1 and h[i] % h[i + 1] == 0:
            i += 1
        end = i

        s = 0
        count = 0
        b = sorted(a[start:end + 1])
        for j in b:
            s += j
            if s >= k:
                ans = max(ans, count)
                break

            count += 1
        i += 1    
        ans = max(ans, count) 

        


    print(ans)

