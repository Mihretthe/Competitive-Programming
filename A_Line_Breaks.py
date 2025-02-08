for _ in range(int(input())):
    n, m = map(int, input().split())
    c = 0
    ss = 0
    
    for _ in range(n):
        s = input()
        ss += len(s)

        if ss <= m:
            c += 1
        else:
            flag = False
    print(c)