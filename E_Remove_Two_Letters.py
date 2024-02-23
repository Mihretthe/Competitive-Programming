for _ in range(int(input())):
    n = int(input())
    s = input()

    
    count = 1
    visit = set()
    l = 0
    r = 2

    while r < n:
        if s[l] != s[r]:
            count += 1
        l += 1
        r += 1            

    print(count)