
for _ in range(int(input())):
    ans = "Division"
    n = int(input())
    if n >= 1900:
        ans += " 1"
    elif n >= 1600:
        ans += " 2"
    elif n >= 1400:
        ans += " 3"
    else:
        ans += " 4"
    print(ans)