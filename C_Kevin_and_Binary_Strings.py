from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())


def solve():
    s = S()
    first_zero = -1

    for i in range(len(s)):
        if s[i] == "0":
            first_zero = i 
            break
    
    if first_zero == -1:
        print(1, len(s), 1, 1)
    else:
        num = int(s, 2)
        k = len(s) - first_zero
        ans = [1, len(s)]
        left = 0
        right = 0
        maxi = 0
        for i in range(len(s) - k + 1):
            a = int(s[i: i + k], 2)
            if num ^ a > maxi:
                maxi = num ^ a
                left = i + 1
                right = i + k

        ans.append(left)
        ans.append(right)
        
        print(*ans)

 
T = I()
for _ in range(T):
    solve()