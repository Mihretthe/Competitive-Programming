for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    # for i in range(n):
    #     if a[i] in a[i + 2:]:
    #         print("YES")
    #         break
    # else:
    #     print("NO")

    occur = {}

    for i in range(n - 1, -1, -1):
        if a[i] in occur:
            if occur[a[i]] - i >= 2 :
                print("YES")
                break
        else:
            occur[a[i]] = i
    else:
        print("NO")
