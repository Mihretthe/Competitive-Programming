for _ in range(int(input())):
    n, d = map(int, input().split())
    a = list(map(int, input().split()))

    m = max(a)

    if m > d:
        a.sort()
        if a[0] + a[1] <= d:
            print("YES")
        else:
            print("NO")
    else:
        print("YES")

