from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())

from collections import Counter, defaultdict

def solve():
    n = I()
    u = IL()
    s = IL()
    array = list(zip(u, s))
    array.sort(reverse = True)
    
    counter = Counter(u)
    indices = defaultdict(int)

    prefix = [array[0][1]]
    index = array[0][0]
    for i in range(1, n):
        a, b = array[i]
        if index == a:
            prefix.append(prefix[-1] + b)
        else:
            index = a
            prefix.append(b)
    
    for i in range(n):
        if array[i][0] not in indices:
            indices[array[i][0]] = i

    answer = []

    for i in range(1, n + 1):
        ans = 0
        dels = []
        for key, val in counter.items():
            if val < i:
                dels.append(key)
                continue

            length = val
            MOD = val % i 
            length = length - MOD - 1

            index = indices[key]
            ans += (prefix[index + length])
        answer.append(ans)

        for i in dels:
            del counter[i]

    print(*answer)

    
 
 
 

T = I()
for _ in range(T):
    solve()