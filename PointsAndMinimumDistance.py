def pair(a, n):
    a.sort()
    x = a[:n]
    y = a[n:][::-1]    
    print(x[-1] - x[0] + y[0] - y[-1])
    for i in range(n):
        print(x[i], y[i])
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    pair(a,n)


