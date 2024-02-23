for _ in range(int(input())):
    n = int(input())
    a = input()
    b = input()

    for i in range(n):
        if a[i] == "G" and b[i] == "R" or a[i] == "B" and b[i] == "R" or a[i] == "R" and b[i] == "G" or a[i] == "R" and b[i] == "B":
            print("NO")
            break
    else:
        print("YES")