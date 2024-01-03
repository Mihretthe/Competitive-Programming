from collections import Counter

for _ in range(int(input())):
    n = int(input())
    a = input().split()
    b = input().split()
    c = input().split()

    strings = a + b + c
    counter = Counter(strings)
    ans = []

    a_gets = 0
    b_gets = 0
    c_gets = 0
    for i in range(n):
        if counter[a[i]] == 1:
            a_gets += 3
        elif counter[a[i]] == 2:
            a_gets += 1

        if counter[b[i]] == 1:
            b_gets += 3
        elif counter[b[i]] == 2:
            b_gets += 1
        
        if counter[c[i]] == 1:
            c_gets += 3
        elif counter[c[i]] == 2:
            c_gets += 1

    print(a_gets, b_gets, c_gets)