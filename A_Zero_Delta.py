from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())


def solve():
    n, k = II()
    a = IL()

    index = 0
    while k and index < n - 1:
        num = a[index]
        if k >= num:
            a[-1] += num
            k -= num
            num = 0
            a[index] = num
        else:
            num -= k
            a[-1] += k
            k = 0
            a[index] = num
        index += 1

    print(*a)

 
 
 
T = I()
for _ in range(T):
    solve()