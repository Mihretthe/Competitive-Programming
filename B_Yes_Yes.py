for _ in range(int(input())):
    s = input()
    lower = "Yes"
    
    for i in range(len(s)):
        if s[i] not in lower:
            print("NO")
            break
        if i == len(s) - 1:
            continue

        if (s[i ] == "Y" and s[i + 1] == "s") or (s[i ] == "Y" and s[i + 1] == "Y") or (s[i ] == "e" and s[i + 1] == "e") or (s[i ] == "e" and s[i + 1] == "Y") or (s[i ] == "s" and s[i + 1] == "e") or (s[i ] == "s" and s[i + 1] == "s"):
            print("NO")
            break
    else:
        print("YES")