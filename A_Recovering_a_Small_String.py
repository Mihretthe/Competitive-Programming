letters = "abcdefghijklmnopqrstuvwxyz"

for _ in range(int(input())):
    n = int(input())

    if n <= 28:
        print("aa" + letters[n - 1 - 2])
    elif n <= 53:
        print("a"+letters[n - 27 - 1] + "z")
    else:
        print(letters[n - 52 - 1] + "zz")
