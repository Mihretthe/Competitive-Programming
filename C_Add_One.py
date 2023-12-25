def handle(n):
    s = []
    while n > 0:
        s.append(str(n%10 + 1)[::-1])
        n //= 10
    
    return int("".join(s)[::-1])
    

for _ in range(int(input())):
    n, m = map(int, input().split())
    a = ""
    for i in range(m):
        n = handle(n)

    print(len(str(n)) % 1000000007)
        
