
for _ in range(int(input())):
    n = int(input())
    s = [i for i in input()]
    indexes = set()
    count = 0

    l = 0
    r = 1

    while r < n:
        if s[l] == "A" and s[r] == "B":
            s[l], s[r] = s[r], s[l]
            count += 1
            indexes.add(l)
            if l > 0 and s[l - 1] == "A" and (l - 1) not in indexes:
                l -= 1
                r -= 1
            else:
                l += 1
                r += 1
        else:
            l += 1
            r += 1
    print(count)

    
    
        






