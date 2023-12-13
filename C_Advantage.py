for _ in range(int(input())):
    n = int(input())
    s = list(map(int, input().split()))

    b = sorted(s)

    first = b[-1]
    second = b[-2]

    ans = []

    for i in s:
        if i == first:
            ans.append(i - second)
        else:
            ans.append(i - first)

    print(*ans)
