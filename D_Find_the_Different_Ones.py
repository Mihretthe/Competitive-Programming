for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    q = int(input())

    table = [-1] * n
    val = n - 1
    for i in range(1, n):
        table[i] = table[i - 1]
        if a[i] != a[i - 1]:
            table[i] = i - 1
    # print(table)

    for __ in range(q):
        l, r = map(int, input().split())
        l -= 1
        r -= 1

        if table[r] < l:
            print(-1,-1)
        else:
            print(table[r] + 1, r + 1)

    
    print()