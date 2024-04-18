n = int(input())
a = list(map(int, input().split()))


if n == 1:
    print(0)
else:
    ans = []
    index = 0

    while index < n:
        start = index
        end = index
        while end < n - 1 and a[end] + 1 == a[end + 1]:
            end += 1
            index += 1
        ans.append((start, end))
        index += 1
    maxi = 0

    for start, end in ans:
        if end < n - 1 and start > 0:
            maxi = max(maxi, end - start - 1)
        elif start > 0 and end == n - 1:
            if a[end] == 1000:
                maxi = max(maxi, end - start)
            else:
                maxi = max(maxi, end - start - 1)
        elif start == 0 and end < n - 1:
            if a[start] == 1:
                maxi = max(maxi, end - start)
            else:
                maxi = max(maxi, end - start - 1)
        elif start == 0 and end == n - 1:
            if a[0] == 1:
                maxi = max(maxi, end - start)
            elif a[end] == 1000:
                maxi = max(maxi, end - start)
            else:
                maxi = max(maxi, end - start - 1)

    print(maxi)