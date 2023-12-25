for _ in range(int(input())):
    n = list(input())
    ans = []
    k = 0

    for i in range(len(n) - 1, -1, -1):
        if n[i] != 0:
            if int("".join(n[i:])) != 0:
                ans.append("".join(n[i:]))
                n[i] = "0"
                k += 1
    print(k)
    print(*ans)