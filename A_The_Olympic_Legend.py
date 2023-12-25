for _ in range(int(input())):
    runners = list(map(int, input().split()))
    a = runners[0]
    runners.sort()

    print(4 - runners.index(a) - 1)

