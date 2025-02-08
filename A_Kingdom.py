# import sys
# from collections import Counter, defaultdict, deque
# from bisect import bisect_right, bisect_left
# from math import ceil


# def ii(): return int(sys.stdin.readline().strip())
# def sti(): return sys.stdin.readline().strip()
# def twi(): return map(int, sys.stdin.readline().strip().split())
# def lsti(): return list(map(int, sys.stdin.readline().strip().split()))
# def slsti(): return sorted(list(map(int, sys.stdin.readline().strip().split())))
# def spacestr(): return map(str, sys.stdin.readline().strip().split())
# def lis(): return list(sys.stdin.readline().strip())
# def slis(): return sorted(list(map(str, sys.stdin.readline().strip().split())))

# n, k = lsti()
# job = lsti()
# pers = lsti()

# count = 0

# s = len(set(job[:k]))

# count = k - s
# print(count)
# arr = []
# arr = pers[:k]
# arr.sort()
# ans = 0
# i = 0
# counter = Counter(job)
# dic = defaultdict(int)

# for i in range(1, n + 1):
#     if counter[i] > 1:
#         dic[]


from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())

from collections import defaultdict

def solve():
    n, k = II()

    a = IL()
    b = IL()

    # counter = defaultdict(int)
    collect = defaultdict(list)

    for i in range(n):
        collect[a[i]].append(b[i])
    
    left = k - len(collect)
    concat = []
    # print(collect)
    for key, value in collect.items():
        value.sort()
        if len(value) > 1:
            value = value[:-1]        
            concat.extend(value)

    concat.sort()

    ans = 0

    # print(concat, left)

    for i in range(left): 
        ans += concat[i]

    print(ans)
    

    
 
 
 
 
T = 1
for _ in range(T):
    solve()