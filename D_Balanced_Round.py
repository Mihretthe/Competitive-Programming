
for _ in range(int(input())):
    n, k = map(int, input().split())
    nums = list(map(int, input().split()))

    problems = 0

    nums.sort()
    count = 1

    for i in range(n - 1):
        if abs(nums[i + 1] - nums[i]) <= k:
            count += 1
        else:
            problems = max(count, problems)
            count = 1

    problems = max(count, problems)
    print(n - problems)


