for _ in range(int(input())):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))

    visit = set()
    s = ["B"] * m

    for i in range(n):
        val = m - a[i] 
        minimum = min(val, a[i] - 1)
        maximum = max(val, a[i] - 1)
        
        if minimum in visit:
            s[maximum] = "A"
            visit.add(maximum)
        else:
            s[minimum] = 'A'
            visit.add(minimum)
    print("".join(s))