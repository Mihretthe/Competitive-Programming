# from collections import defaultdict

for _ in range(int(input())):
    n = int(input())
    s = input()

    #Code Doesn't Work
    # checker = defaultdict(int)
    
    # for i in range(0, n - 1, 2):
    #     checker[s[i:i + 2]] += 1
    #     if checker[s[i:i + 2]] > 1:
    #         print("YES")
    #         break
    # else:
    #     print("NO")

    at = 0
    for i in range(2, n):
        if s[at:i] in s[i:]:
            print("YES")
            break
        at += 1

    else:
        print("NO")


    # Try this question using set

    # s = s[::-1]
    # pairs = set()
    # for i in range(n - 1):
    #     if s[i:i+2] in pairs:
    #         print("YES")
    #         break
    #     pairs.add(s[i:i+2])

    # else:
    #     print("NO")