n = int(input())
segments = input()
count = 1
if "MM" in segments or "YY" in segments or "CC" in segments:
    print("No")
else:
    if segments[0] == "?" or segments[-1] == "?":
        print("Yes")
    else:
        flag = False
        for i in range(1, n - 1):
            if segments[i] == "?" and segments[i - 1] == segments[i + 1]:
                flag = True
            elif segments[i] == "?" and (segments[i - 1] == "?" or segments[i + 1] == "?"):
                flag = True
        if flag:
            print("Yes")
        else:
            print("No")
