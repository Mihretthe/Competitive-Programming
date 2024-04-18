for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    indices = []

    for i in range(n):
        if a[i] == 1:
            indices.append(i)

    print(a[indices[0] : indices[-1]].count(0))