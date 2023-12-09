testcases = int(input())

for _ in range(testcases):
    n = int(input())
    checker = 0
    start = 0
    end = 0
    for i in range(1,n):
        checker += i
        if checker == n:
            end = i + 1
            break
        elif checker > n:
            start -= 1
            end = i
            break
    # if start < 0:
    #     start = 1
    #     while checker != n:
    #         checker -= start
    #         start += 1
    print(start, end)