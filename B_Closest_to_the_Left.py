n, k = map(int, input().split())
a = list(map(int, input().split()))
q = list(map(int, input().split()))

for num in q:

    left = -1
    right = n 

    while left + 1 < right:
        mid = left + (right - left) // 2

        if a[mid] > num:
            right = mid
        else:
            left = mid

    print(right)