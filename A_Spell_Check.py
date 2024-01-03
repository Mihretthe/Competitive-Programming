for _ in range(int(input())):
    n = int(input())
    s = input()
    if n != 5:
        print("NO")
        continue
    checker = ["T","i","m","u","r"]

    for i in s:
        if i not in checker:
            print("NO")
            break
        checker.remove(i)
    else:
        print("YES")
