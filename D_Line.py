def solve(s, n):
    R = list(range(n - 1, -1, -1))
    L = R[::-1]
    values = []
    for i in range(n):
        if s[i] == "L":
            values.append(i)
        else:
            values.append(n - 1 - i)

    ans = []
    enumerated = list(enumerate(values))
    enumerated.sort(key = lambda x : x[1])
    max_sum = sum(values)

    for index, value in enumerated:        
        values[index] = max(L[index], R[index])
        if values[index] > value:
            max_sum += (values[index] - value)
        ans.append(max_sum)

    return  ans

for _ in range(int(input())):
    n = int(input())
    s = input()

    print(*solve(s,n))