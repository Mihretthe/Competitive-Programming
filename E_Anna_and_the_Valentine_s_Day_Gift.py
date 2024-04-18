for _ in range(int(input())):
    n, m = map(int, input().split())
    a = list(input().split())
    a.sort(reverse = True)

    change = 0

    for i in range(n):
        num = a[i]
        length = len(num)
        if "0" in num:
            end = length - 1
            while end >= 0:
                if num[end] != "0":
                    break
                end -= 1

            change += (end + 1)
        else:
            change += length

    if change >= m:
        print("Sasha")
    else:
        print("Anna")