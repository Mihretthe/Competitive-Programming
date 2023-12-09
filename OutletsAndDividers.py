def howMany(n, m, a):
    if n <= 2:
        return 0
    a.sort(reverse = True)
    prefix = 0
    for i in range(m):
        prefix += a[i]
        if prefix >= n:
            return i + 1
    return -1
for _ in range(int(input())):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    print(howMany(n,m,a))


