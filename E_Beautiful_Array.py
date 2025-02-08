from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())

from random import randint

from collections import defaultdict, Counter

def solve():
    n, k = II()
    a = IL()

    counter = Counter(a)
    
    remainder = defaultdict(list)

    array = []

    for key, value in counter.items():
        if value % 2:
            array.append(key)

    if len(array) == 1:
        print(0)
        return
    
    # print(array, n )

    for num in array:
        remainder[num % k].append(num)

    
    flag = False
    ans = 0

    
    


    for key, value in remainder.items():
        if flag and len(value) == 1:
            print(-1)
            return
        if len(value) == 1:
            flag = True
            continue
        
        value.sort()

        if len(value) % 2:
            maxi = 0
            ind = 0
            for i in range(len(value) - 1):              
                
                if value[i + 1] - value[i] > maxi:
                    ind = i 
                    maxi = value[i + 1] - value[i]

            # value = value[:ind] + value[ind + 1:]
            # print(value)


        
        
        count = 0
        for i in range(0, len(value) - 1, 2):
            count += (value[i + 1] - value[i]) // k

        ans += count

    print(ans)


        

    
    
        
 
 
 
T = I()
for _ in range(T):
    solve()