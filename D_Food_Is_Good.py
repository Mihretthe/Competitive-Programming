for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    simon = sum(a)

    aman = 0
    s = 0
    flag = True
    allZero = True

    for i in range(n):
        if a[i] != 0:
            allZero = False
        if a[i] < 0:
           flag = False
           s = 0
        else:
            s += a[i]
        aman = max(s, aman)
    if flag:
        if allZero:
            print("NO")
        else:
            print("YES")
        continue
    if simon > aman:
        print("YES")
    else:
        print("NO")

             