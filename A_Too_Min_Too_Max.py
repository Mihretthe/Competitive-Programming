for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    a.sort()

    i = 0
    l = 1
    j = -2
    r = -1

    print(abs(a[r] - a[l]) + abs(a[r] - a[i]) + abs(a[j] - a[l]) + abs(a[j] - a[i]))