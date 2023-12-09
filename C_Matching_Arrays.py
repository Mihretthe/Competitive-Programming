for _ in range(int(input())):
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    beautiful = []

    for i in range(n):
        if a[i] > b[i]:
            beautiful.append(i)

    if len(beautiful) == x:
        print("YES")
        print(*b)
    else:
        c = sorted(a)
        d = sorted(b)
        count = 0
        for i in range(n):
            if [ci] > d[i]:
                count += 1

        if count == x:
            print("YES")
            print()
        else:
            pass

