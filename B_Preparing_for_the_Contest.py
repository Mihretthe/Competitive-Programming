for _ in range(int(input())):
    n, k = map(int, input().split())

    problems = list(range(n, 0, -1))
    problems = problems[k:] + problems[:k][::-1]

    print(*problems)