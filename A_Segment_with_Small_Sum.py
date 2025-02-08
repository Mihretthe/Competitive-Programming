from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())


def solve():
    n, k = II()
    nums = IL()

    left = 0
    max_length = 0
    total = 0
    for right in range(n):
        total += nums[right]

        while total > k:
            total -= nums[left]
            left += 1

        max_length = max(max_length, right - left + 1)

    print(max_length)
 
 
 
 
T = 1
for _ in range(T):
    solve()