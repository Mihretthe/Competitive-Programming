n = int(input())
segments = input()
count = 1
if "MM" in segments or "YY" in segments or "CC" in segments:
    print("NO")
else:
    if segments[0] == "?" or segments[-1] == "?":
        print("YES")
    else:
        i = 1
        while i < n - 1:
            if segments[i] == "?":
                if segments[i + 1] == "?" or segments[i - 1] == segments[i + 1]:
                    print("YES")
                    break
                elif segments[i - 1] != segments[i + 1]:
                    print("NO")
                    break



