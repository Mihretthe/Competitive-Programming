def I(): return int(input())
 
def II(): return map(int, input().split())
 
def IL(): return list(map(int, input().split()))
 
def SIL(): return sorted(map(int, input().split()),)

def S() : return input()

def SL() : return list(input().split())

from math import ceil
 
def solve():
    n = I()
    a = list(map(int, list(input())))
    first = a[:n]
    second = a[n:]

    first.sort()
    second.sort()

    flag = first[0] < second[0]
    if first[0] == second[0]:
        print("NO")
        return 


    if flag:
        for i in range(1, n):
            if first[i] >= second[i]:
                print("NO")
                break
        else:
            print("YES")
    else:
        for i in range(1, n):
            if first[i] <= second[i]:
                print("NO")
                break
        else:
            print("YES")
 
 
 
 
T = 1
for _ in range(T):
    solve()