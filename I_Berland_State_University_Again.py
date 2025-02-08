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

t = int(sys.stdin.readline().strip())

for _ in range(t):
    a, b, c = map(int, sys.stdin.readline().strip().split())
    sums = a + b + c
    tar = ceil(sums/3)

    ass = [a, 0, 0]
    bas = [0, b , 0]
    cp = [0, 0, c]
    if a < tar:
        if bas[2] < bas[1]:
            left = tar - a
            a += left
            ass[0] += left
            b -= left
            bas[1] -= left

    if a > tar:
        if bas[2] == 0:
            left = a - tar
            b += left
            bas[0] += left
            a -= left
            ass[0] -= left
    if c < tar:
        if bas[0] < bas[1]:
            left = tar - c
            c += left
            cp[1] += left
            b -= left
            bas[1] -= left
    if c > tar:
        if bas[0] == 0:
            left = c - tar
            b += left
            bas[2] += left
            c -= left
            cp[2] -= left

    ls = [a, b, c]
    print(max(ls))