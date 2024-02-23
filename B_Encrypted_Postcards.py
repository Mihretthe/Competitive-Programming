for _ in range(int(input())):
    n = int(input())
    s = input()
    a = ""

    l = 0 
    r = 1
    while r < n:
        if s[l] == s[r]:
            a += s[l]
            l = r + 1
            r += 2
        else:
            r += 1
    print(a)
