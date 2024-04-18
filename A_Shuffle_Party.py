for _ in range(int(input())):
    n = int(input())
    if n == 1:
        print(1)
        continue
    if n == 2:
        print(2)
        continue
    
    p = 1
    while p * 2 <= n:
        p <<= 1
    
    print(p)
