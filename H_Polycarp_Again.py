import sys
from collections import Counter, defaultdict, deque
from bisect import bisect_right, bisect_left
from math import ceil


def ii(): return int(sys.stdin.readline().strip())
def sti(): return sys.stdin.readline().strip()
def twi(): return map(int, sys.stdin.readline().strip().split())
def lsti(): return list(map(int, sys.stdin.readline().strip().split()))
def slsti(): return sorted(list(map(int, sys.stdin.readline().strip().split())))
def spacestr(): return map(str, sys.stdin.readline().strip().split())
def lis(): return list(sys.stdin.readline().strip())
def slis(): return sorted(list(map(str, sys.stdin.readline().strip().split())))

n, k =  map(int, sys.stdin.readline().strip().split())
nums = list( map(int, sys.stdin.readline().strip().split()))

ans = []
res = True
x = sum(nums)
fac = x // k
if x % k != 0:
    print("No")
    exit()

sums = 0
cnt =  0
for i in range(n):
    sums += nums[i]
    cnt += 1
    # if sums < fac:
    #     cnt += 1
    if sums == fac:
        ans.append(cnt)
        cnt = 0
        sums = 0
    elif sums > fac:
        res = False
        break

if res:
    print("Yes")
    print(*ans)
else:
    print("No")