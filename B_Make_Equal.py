for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    portion = sum(a) // n

    remain = 0

    for i in range(n):
        if a[i] + remain < portion:
            print("NO")
            break
        remain += (a[i] - portion)
    else:
        print("YES")