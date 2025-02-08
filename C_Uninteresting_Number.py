from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())

from collections import Counter

def solve():
    
    nums = list(map(int, list(input())))
    counter = Counter(nums)

    total = sum(nums) 
    mod = total % 9

    need = 9 - mod

    if need == 8:
        if counter[2] >= 4:
            print('YES')
        elif counter[2] >= 1 and counter[3] >= 1:
            print("YES")
        else:
            print("NO")
    elif need == 7:
        if (counter[3] >= 1 and counter[2] >= 5) or (counter[3] >= 2 and counter[2] >= 2) or (counter[2] >= 8):
            print("YES")
        else:
            print("NO")
    elif need == 6:
        if counter[3] >= 1 or counter[2] >= 3:
            print('YES')
        else:
            print("NO")
    elif need == 5:
        if (counter[2] >= 7) or (counter[3] >= 1 and counter[2] >= 4) or (counter[3] >= 2 and counter[2] >= 1):
            print("YES")
        else:
            print("NO")
    elif need == 4:
        if counter[2] >= 2:
            print("YES")
        else:
            print("NO")
    elif need == 3:
        if (counter[3] >= 2) or (counter[3] >= 1 and counter[2] >= 3) or counter[2] >= 6:
            print("YES")
        else:
            print("NO")
    elif need == 2:
        if counter[2] >= 1:
            print("YES")
        else:
            print("NO")
    elif need == 1:
        if (counter[2] >= 5) or (counter[2] >= 2 and counter[3] >= 1):
            print("YES")
        else:
            print('NO')
    else:
        print("YES")        
 
 
 
 
T = I()
for _ in range(T):
    solve()

