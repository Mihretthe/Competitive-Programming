for _ in range(int(input())):
    a, b, l = map(int, input().split())

    val = 0
    for_a = []
    for_b = []
    visit = set()

    while a**val <= l:
        if l % a**val == 0:
            for_a.append(a**val)
        val += 1

    val = 0
    while b**val <= l:
        if l % b**val == 0:
            for_b.append(b**val)
        val += 1

    count = 0

    for i in for_a:
        for j in for_b:
            if (i*j) in visit:
                continue
            visit.add(i*j)
            if l % (i * j) == 0:
                count += 1

    print(count)

