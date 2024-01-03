x, k = map(int, input().split())
for _ in range(k):
    a = list(map(int, input().split()))
    a.sort()
    i = 0
    while x + a[i] < 0 and i < len(a):
        i += 1
    x += a[i]         

print(x)
