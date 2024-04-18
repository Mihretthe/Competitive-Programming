
def I(): return int(input())
 
def II(): return map(int, input().split())
 
def IL(): return list(map(int, input().split()))
 
def SIL(): return sorted(map(int, input().split()),)


def solve():
    n = I()
    s = list(input())
    count = 0
    
    for i in range(n - 1):
        string = "".join(s[i: i + 3])
        if string == "map" or string == "pie":
            count += 1
            s[i+2] = "_"
    print(count)

    



T = I()
for _ in range(T):
    solve()