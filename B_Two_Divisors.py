"""
from the largest one till we find an integer that is a divisible by the smaller one but check till the larger one there is no divisor in between
"""
for _ in range(int(input())):
    a, b = map(int, input().split())
    flag = True
    s = b
    while flag:
        s += b
        if (s) % a == 0:            
            i = a + a
            while i < b:
                if s % i == 0:
                    break
                i += a
            else:
                flag = False
        

    print(s)
