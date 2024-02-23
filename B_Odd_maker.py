for _ in range(int(input())):
    n, q = map(int, input().split())
    nums = list(map(int, input().split()))

    prefix_sum = [0]
    for i in range(n):
        prefix_sum.append(prefix_sum[-1] + nums[i])

    for _ in range(q):
        l, r, k = map(int, input().split())
        num = (r - l + 1) * k
        sub = prefix_sum[r] - prefix_sum[l - 1]

        if (prefix_sum[-1] - sub + num) % 2 == 1:
            print("YES")
        else:
            print("NO")