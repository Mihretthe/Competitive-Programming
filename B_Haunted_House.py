def S(): return input()

def I(): return int(input())
 
def II(): return map(int, input().split())
 
def IL(): return list(map(int, input().split()))
 
def SIL(): return sorted(map(int, input().split()),)

from collections import deque
 
def solve():
    n = I()
    binary = S()[::-1]
    ans = []
    indices = deque()


    for i in range(n):
        if binary[i] == "0":
            indices.append(i)

    for i in range(n):
        if not ans:
            if binary[i] == "0" :
                ans.append(0)
                indices.popleft()
            else:
                if indices:
                    ans.append((indices.popleft() - i))
                else:
                    ans.append(-1)
        else:
            if not indices:
                ans.append(-1)
            else:
                ans.append(ans[-1] + (indices.popleft() - i))
        

    print(*ans)


T = I() 
for _ in range(T):
    solve()