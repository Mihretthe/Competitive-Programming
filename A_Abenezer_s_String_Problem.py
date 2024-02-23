for _ in range(int(input())):
    length = int(input())
    s = input()
    letters = "abcdefghijklmnopqrstuvwxyz"
    s = sorted(s)
    print(letters.index(s[-1]) + 1)