for _ in range(int(input())):
    n, m, k = map(int, input().split())
    a = set(map(int, input().split()))
    b = set(map(int, input().split()))

    count_a = 0
    count_b = 0

    nums = list(range(1, k + 1))
    for i in nums:        
        if i not in a and i not in b:
            print("NO")
            break
        elif i in a and i in b:
            continue
        elif i in a:
            count_a += 1
        elif i in b:
            count_b += 1
        if count_b > k // 2 or count_a > k // 2:
            print("NO")
            break
    else:
        print("YES")

