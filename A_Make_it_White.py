for _ in range(int(input())):
    n = int(input())
    s = input()

    indices = []

    for i in range(n):
        if s[i] == "B":
            indices.append(i)
    
    print(indices[-1] - indices[0] + 1)