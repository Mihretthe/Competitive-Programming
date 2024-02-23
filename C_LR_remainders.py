from math import prod


for _ in range(int(input())):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    s = input()
    # print(a)
    product = 1
    answer = []
    r = n - 1
    l = 0
    s_num = []

    for i in s:
        if i == "L":
            s_num.append(l)
            l += 1
        else:
            s_num.append(r)
            r -= 1
    for i in range(n - 1):
        product = (product * a[s_num[i]]) % m

        answer.append(product)
    
    print(*answer)