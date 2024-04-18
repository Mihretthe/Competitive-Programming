for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    a.sort()
    max_score = 0

    for i in range(0, 2*n, 2):
        max_score += a[i]

    print(max_score)