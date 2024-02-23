for _ in range(int(input())):
    n, k = map(int, input().split())

    letters = "abcdefghijklmnopqrstuvwxyz"

    answer = letters[:k] * n

    print(answer)