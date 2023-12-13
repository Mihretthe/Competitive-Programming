for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0

    first_zero = a[:]
    last_one = a[:]

    if 0 in first_zero:
        idx = first_zero.index(0)
        first_zero[idx] = 1
        count = 0
        r = n - 1
        zeros = 0

        while r >= 0:
            if first_zero[r] == 0:
                zeros += 1
            elif first_zero[r] == 1:
                count += zeros
            r -= 1

        ans = max(count, ans)
    
    if 1 in last_one:
        a.reverse()
        idx = a.index(1)
        last_one[n - idx - 1] = 0

        count = 0
        r = n - 1
        zeros = 0

        while r >= 0:
            if last_one[r] == 0:
                zeros += 1
            elif last_one[r] == 1:
                count += zeros
            r -= 1

        ans = max(count, ans)

    print(ans)