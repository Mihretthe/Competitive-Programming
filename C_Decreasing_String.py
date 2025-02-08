from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())

ans = []

def solve():
    
    s = list(S())
    pos = I() - 1

    i = 0
    stack = []
    length = len(s)

    while i < len(s):
        if pos < length:
            stack.extend(s[i:])
            ans.append(stack[pos])
            return
        if stack and stack[-1] > s[i]:
            stack.pop()
            pos -= length
            length -= 1
        else:
            stack.append(s[i])
            i += 1
    
    while pos >= length:
        pos -= length
        length -= 1

    ans.append(stack[pos])


 
 
 
 
T = I()
for _ in range(T):
    solve()

print("".join(ans))