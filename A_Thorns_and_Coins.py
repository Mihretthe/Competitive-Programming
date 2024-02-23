for _ in range(int(input())):
    n = int(input())
    s = input()
    count = 0

    index = n
    if "**" in s:
        index = s.index("**")

    print(s[:index + 1].count("@"))