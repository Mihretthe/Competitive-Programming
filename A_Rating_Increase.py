for _ in range(int(input())):
    ab = input()

    a = ab[0]

    for i in range(1, len(ab)):
        if ab[i] != "0":
            break
        else:
            a += ab[i]

    b = ab[i:]
    if int(a) == int(b):
        print(-1)
    else:
        print(a, b)