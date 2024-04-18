def isPrime(num):
    d = 2
    while d * d < num:
        if num % d == 0:
            return False
        d += 1
    return True
from math import sqrt, ceil

def factorize(num):
    ans = []

   # first collect all prime factoriztions till root n
    
    for i in range(2, num + 1):
        if isPrime(i) and num % i == 0:
            ans.append(i)
    
    return ans


# print(factorize(34))
num = int(input())
count = 0

for i in range(1, num + 1):
    if len(factorize(i)) == 2:
        count += 1

print(count)
