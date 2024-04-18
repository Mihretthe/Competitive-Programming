n, k = map(int, input().split())
a = list(map(int, input().split()))
q = list(map(int, input().split()))

for num in q:

    left = 0
    right = n - 1

    while left <= right:
        mid = left + (right - left) // 2
        if a[mid] == num:
            print("YES")
            break
        elif a[mid] < num:
            left = mid + 1
        else:
            right = mid - 1
    else:
        print("NO")