for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    c = list(map(int,input().split()))
    ans = 0

    a = list(enumerate(a))
    a.sort(reverse = True, key = lambda x : x[1])
    a = a[:3]

    b = list(enumerate(b))
    b.sort(reverse = True, key = lambda x : x[1])
    b = b[:3]

    c = list(enumerate(c))
    c.sort(reverse = True, key = lambda x : x[1])

    
    
    for i in range(3):
        for j in range(3):
            if b[j][0] != a[i][0]:
                for k in range(3):
                    if c[k][0] != b[j][0] and c[k][0] != a[i][0]:
                        ans = max(ans, a[i][1] + b[j][1] + c[k][1])

    print(ans)


