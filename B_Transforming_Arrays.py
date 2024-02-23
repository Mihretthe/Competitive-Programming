from collections import defaultdict

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    indices = defaultdict(list)

    for i in range(n):
        indices[a[i]].append(i)

    for i in range(n):
        if a[i] == b[i]:
            continue
        if b[i] < 0:
            if -1 in indices and indices[-1][0] < i:
                continue
            else:
                print("NO")
                break
        elif b[i] > 0:
            if 1 in indices and indices[1][0] < i:
                continue
            else:
                print("NO")
                break
        elif b[i] == 0:
            if a[i] == 1 and -1 in indices and indices[-1][0] < i:
                continue
            elif a[i] == -1 and 1 in indices and indices[1][0] < i:
                continue
            else:
                print("NO")
                break
    else:
        print("YES")