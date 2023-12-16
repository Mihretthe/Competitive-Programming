def sumDigits(num):
    result = 0

    while num > 0:
        result += num % 10
        num //= 10

    return result


for _ in range(int(input())):
    n, q = map(int, input().split())
    a = list(map(int, input().split()))

    s = []

    for num in a:
        s.append(sumDigits(num))
   
    
    for __ in range(q):
        query = list(map(int, input().split()))
        if len(query) == 3:
            l, r = query[1] - 1, query[2] - 1
            a[l:r + 1] = s[l : r + 1]
            for i in range(l, r + 1):
                s[i] = sumDigits(s[i])
        else:
            print(a[query[1] - 1])
            
            
