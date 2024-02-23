for _ in range(int(input())):
    n = int(input())
    s = list(map(int, input().split()))

    sorted_s = sorted(s)
    max_num = sorted_s[-1]
    next = sorted_s[-2]

    ans = []

    for i in range(n):
        if s[i] == max_num:
            ans.append(s[i] - next)
        else:
            ans.append(s[i] - max_num)
    print(*ans)