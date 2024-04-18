for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    a.sort()

    i = 0
    ans = 0

    while i < n and a[i] <= 0:
        ans += a[i]
        i += 1
    
    ans = 0 - ans
    ans += sum(a[i:])

    print(ans)