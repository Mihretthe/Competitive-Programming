from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())

def solve():
    n = I()
    t = S()
    letters = "0abcdefghijklmnopqrstuvwxyz"
    ans = []
    index = n - 1
    while index >= 0:
        if t[index] == "0":
            num = int(t[index - 2: index])
            ans.append(letters[num])
            index -= 3
        else:
            num = int(t[index])
            ans.append(letters[num])
            index -= 1

    print("".join(ans[::-1]))



 
 
 
 
T = I()
for _ in range(T):
    solve()