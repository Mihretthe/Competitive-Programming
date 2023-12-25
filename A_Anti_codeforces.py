for _ in range(int(input())):
    s = input()
    c = "codeforces"
    count = 0
    for i in range(len(s)):
        if s[i] != c[i]:
            count += 1

    print(count)