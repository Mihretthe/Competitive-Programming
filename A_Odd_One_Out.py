for _ in range(int(input())):
    abc = list(map(int, input().split()))
    for i in abc:
        if abc.count(i) == 1:
            print(i)
            break