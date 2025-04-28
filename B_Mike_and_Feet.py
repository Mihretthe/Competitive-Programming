from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())


def solve():
    n = I()
    a = IL()
    
    next_smaller = [n] * n
    previous_smaller = [0] * n
    
    stack = []
    
    for i in range(n):
        while stack and a[stack[-1]] > a[i]:
            next_smaller[stack.pop()] = i 
        
        stack.append(i)
    stack = []
    for i in range(n - 1, -1, -1):
        while stack and a[stack[-1]] >= a[i]:
            previous_smaller[stack.pop()] = i + 1
        
        stack.append(i)
    # print(sorted(a))   
    # print(previous_smaller)
    # print(next_smaller)
    
    answer = [-1] * n
    
    for i in range(n):
        len_diff = next_smaller[i] - previous_smaller[i]
        answer[len_diff - 1] = max(answer[len_diff - 1], a[i])
    
    maxi = min(a)
    for i in range(n - 1, -1 , -1):
        if answer[i] == -1:
            answer[i] = maxi
        else:
            maxi = max(maxi, answer[i])
            answer[i] = maxi
    
    print(*answer)
        
 
 
 
 
T = 1
for _ in range(T):
    solve()