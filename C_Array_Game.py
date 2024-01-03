for _ in range(int(input())):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    r = []
    
    m = min(a)
    for i in range(n):
        for j in range(i + 1,n):
            r.append((i,j,abs(a[j] - a[i])))

    r.sort(key = lambda x : x[2])

    for i, j, diff in r[:k]:
        a.append(diff)
        if d



    print(a)
    print()
