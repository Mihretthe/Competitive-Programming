for _ in range(int(input())):
    n = int(input())
    a, b, c = input(), input(), input()
    flag = True
    for i, j, k in zip(a,b,c):        
        if i != j and j != k and i != k or i == j and i != k:
            print("YES")
            break
    else:
        print("NO")