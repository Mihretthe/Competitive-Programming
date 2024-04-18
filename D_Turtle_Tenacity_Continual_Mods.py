for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    a.sort()
    if a[0] % a[1] != 0:
        print("YES")
        continue
    prev = a[1]
    for i in range(n):
        if a[i] % a[0] != 0:
            print("YES")
            break
    else:
        print("NO")