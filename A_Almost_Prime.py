from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())

def solve():
    n = I()
    number = 0

    for i in range(2, n + 1):
        num = i
        count = 0
        d = 2
        while d * d <= num:
            flag = False
            while num % d == 0:
                flag = True
                num //= d
            if flag:
                count += 1
            d += 1
        if num > 1:
            count += 1
        if count == 2:
            number += 1

    print(number)


 
 
 
 
T = 1
for _ in range(T):
    solve()
