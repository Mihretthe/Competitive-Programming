for _ in range(int(input())):
    a, b, c = map(int, input().split())
    if a + b == c:
        print("+")
    elif a - b == c:
        print("-")
