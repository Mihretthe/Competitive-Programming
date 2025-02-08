from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())

def solve():
    n, m = II()
    a = IL()

    answer = [0]
    answer2 = [0]

    for i in range(1, n):
        
        if a[i - 1] > a[i]:
            answer.append(answer[-1] + (a[i - 1] - a[i]))
        else:
            answer.append(answer[-1])

    for i in range(n - 2, -1, -1):
        if a[i + 1] > a[i]:
            answer2.append(answer2[-1] + a[i + 1] - a[i])
        else:
            answer2.append(answer2[-1])
    
    answer2 = answer2[::-1]
    

    for _ in range(m):
        s, t = II()
        s, t = s - 1, t - 1
        if s > t:
            print(answer2[t] - answer2[s])
        else:
            print(answer[t] - answer[s])

 
 
 
 
T = 1
for _ in range(T):
    solve()