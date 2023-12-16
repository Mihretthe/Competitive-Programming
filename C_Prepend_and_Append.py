for _ in range(int(input())):
    n = int(input())
    s = input()

    if len(s) == 0:
        print(0)
        continue

    l = 0
    r = n - 1
    while l <= r:
        if s[l] == s[r]:
            break
        r -= 1
        l += 1

    print(r - l + 1)