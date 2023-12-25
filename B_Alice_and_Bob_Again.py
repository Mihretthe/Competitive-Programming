for _ in range(int(input())):
    b = input()

    a = ""

    for i in range(len(b)):
        if i % 2 == 0:
            a += b[i]
    if len(b) % 2 == 0:
        a += b[-1]

    print(a)