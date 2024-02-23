for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    a.sort()

    left = n - 1
    right = n 
    print(a[right] - a[left])