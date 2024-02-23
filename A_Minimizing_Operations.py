for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    maxi = max(a)
    mini = min(a)

    print(maxi - mini)