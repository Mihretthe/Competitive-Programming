def I(): return int(input())
 
def II(): return map(int, input().split())
 
def IL(): return list(map(int, input().split()))
 
def SIL(): return sorted(map(int, input().split()),)

def S() : return input()

def SL() : return list(input().split())

from math import prod

def check(a, b):
    index = 0
    length = len(b)

    for i in a:
        
        if i == b[index]:
            index += 1
        if index >= length:
            return True
    return False

    


def solve():
    t = list(S())
    p = S()
    a = IL()

    high = len(t) - len(p) + 1

    low = 0
    ans = 0

    while low + 1 < high:
        mid = (low + high) // 2
        string = t[:]
        for i in range(mid):
            string[a[i] - 1] = ""
        string = "".join(string)

        if check(string, p):
            ans = max(ans, mid)
            low = mid
        else:
            high = mid
    

    print(ans)



   
T = 1
for _ in range(T):
    solve()