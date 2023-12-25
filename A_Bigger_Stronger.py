from collections import Counter
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    
    if len(set(a)) == n:
        print("YES")
    else:
        print("NO")
    # counter = Counter(a)

    # a = list(counter.values())
    # if len(set(a)) == 1 and a[0] == 1:
    #     print("YES")
    # else:
    #     print('NO')