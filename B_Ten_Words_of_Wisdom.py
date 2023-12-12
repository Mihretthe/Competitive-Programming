for _ in range(int(input())):
    n = int(input())
    ans = 0
    quality = 0

    for i in range(n):
        a, b = map(int, input().split())
        if a > 10:
            continue
        if quality < b:
            ans = i + 1
            quality = b

    print(ans)
