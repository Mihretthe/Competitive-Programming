for _ in range(int(input())):
    n = int(input())
    s = input()

    if n % 2 == 0:
        if s <= s[::-1]:            
            print(s)
        else:
            print(s[::-1] + s)
    else:
        if s > s[::-1]:
            s = s[::-1]
        else:
            s += s[::-1]
        print(s)