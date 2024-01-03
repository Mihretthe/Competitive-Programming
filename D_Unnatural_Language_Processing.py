for _ in range(int(input())):
    n = int(input()) - 1
    s = input()
    v = "ae"
    ans = []

    while n > -1:
        if s[n] in v:
            ans.append(s[n-1:n + 1][::-1])
            n -= 2
        else:
            ans.append(s[n-2:n + 1][::-1])
            n -= 3

    print(".".join(ans)[::-1])