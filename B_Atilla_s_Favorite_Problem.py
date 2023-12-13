t = int(input())

for _ in range(t):
    n = int(input())
    s = input()
    letters = "abcdefghijklmnopqrstuvwxyz"

    s = sorted(s)
    
    ans = letters.index(s[-1])

    print(ans + 1)
