from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())


def solve():
    n = I()
    if n < 3:
        print(-1)
        return 
    if n == 3:
        print(210)
        return
    hashmap = {4: "50", 5: "80", 6 : "170", 7 : "20", 8: "200", 9: "110"}
    if n in hashmap:
        a = hashmap[n]
        ans = "1" + "0" * (n - len(a) - 1) + a
    else:
        mod = n % 6
        if mod not in hashmap:
            mod += 6
        a = hashmap[mod]
        ans = "1" + "0" * (n - len(a) - 1) + a
    print(ans)
 
 
 
 
T = 1
for _ in range(T):
    solve()