for _ in range(int(input())):
    n = int(input())
    s = input()

    alperen = [0,0]

    for i in s:
        if i == "U":
            alperen[1] += 1
        elif i == "D":
            alperen[1] -= 1
        elif i == "L":
            alperen[0] -= 1
        else:
            alperen[0] += 1
        if alperen == [1,1]:
            print("YES")
            break
    else:
        print("NO")

