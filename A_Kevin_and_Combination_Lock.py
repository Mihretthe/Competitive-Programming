def solve():
    s = input()
    s = s.replace("33", "")
    
    if not s or (int(s)) % 33 == 0:
        print("YES")
    else:
        print("NO")

 
 
 
 
T = int(input())
for _ in range(T):
    solve()

