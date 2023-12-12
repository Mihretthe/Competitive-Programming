t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    a.sort()
    a[0] += 1
    product = 1

    for i in a:
        product *= i

    print(product)