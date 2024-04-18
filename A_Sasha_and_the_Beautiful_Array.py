for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    a.sort()
    answer = 0

    for i in range(1, n):
        answer += (a[i] - a[i - 1])

    print(answer)