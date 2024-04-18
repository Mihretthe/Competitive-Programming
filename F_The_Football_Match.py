for _ in range(int(input())):
    s = input()
    n = len(s)
    even = 0
    odd = 0
    remain = 5
    ans = float('inf')

    for i in range(n):
        if i % 2 == 0:
            if s[i] != "0":
                even += 1
            remain -= 1
        else:
            if s[i] == "1":
                odd += 1

        if odd > even + remain:
            ans = min(ans, i+1)
            break
    
    even = 0
    odd = 0
    remain = 5

    for i in range(n):
        if i % 2 == 1:
            if s[i] != "0":
                even += 1
            remain -= 1
        else:
            if s[i] == "1":
                odd += 1

        if odd > even + remain:
            ans = min(ans, i+1)
            break

    print(ans)