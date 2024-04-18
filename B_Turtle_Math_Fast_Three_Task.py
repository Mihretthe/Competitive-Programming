for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    total = sum(a)

    if total % 3 == 0:
        print(0)
        continue

    mod = total % 3
    answer = 3 - mod

    
    for i in range(n):
        if a[i] % 3 == mod:
            print(1)
            break
    else:
        print(answer)