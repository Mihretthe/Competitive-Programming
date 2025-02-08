for i in range(int(input())):
    n = int(input())
    mx = 0
    mn= 1000000
    lst = input().split()
    for j in range(n):
        x = int(lst[j])
        mx = max(mx, x)
        mn = min(mn, x)
    print((mx-mn)*(n-1))