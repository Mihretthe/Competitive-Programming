for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    i = 0
    while i < n - 1:
        if a[i] < 0 and abs(a[i]) >= abs(a[i + 1]):
            a[i], a[i + 1] = (0 - a[i]), (0 - a[i + 1])           
        i += 1
    print(sum(a))
