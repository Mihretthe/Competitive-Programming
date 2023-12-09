for _ in range(int(input())):
    s = input()
    a = s[0]
    b = s[1]

    for i in "abcdefgh":
        if i != a:
            print(i+ b)
    for i in range(1,9):
        if i != int(b):
            print(a + str(i))