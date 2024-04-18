from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())

from math import gcd, lcm

def solve():
    length = I()
    nums = IL()

    b = [nums[0]]

    for i in range(length - 1):
        b.append(lcm(nums[i], nums[i + 1]))

    b.append(nums[-1])

    for i in range(1, length):
        if gcd(b[i - 1], b[i]) != nums[i - 1]:
            print("NO")
            break
    else:
        print("YES")


 
T = I()
for _ in range(T):
    solve()