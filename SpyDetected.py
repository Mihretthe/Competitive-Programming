def detectSpy(a, n):
    for i in range(n):
        if a.count(a[i]) == 1:
            return i + 1
    return 0


for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    print(detectSpy(a, n))