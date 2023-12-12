t = int(input())



for _ in range(t):
    ans = 0
    for i in range(10):
        s = input()
        a = []
        if "X" in s:
            

            for j in range(10):
                if s[j] == "X":
                    a.append((i,j))

            for r, c in a:
                if r == 0 or r == 9 or c == 0 or c == 9:
                    ans += 1
                elif r == 1 or r == 8 or c == 1 or c == 8:
                    ans += 2
                elif r == 2 or r == 7 or c == 2 or c == 7:
                    ans += 3
                elif r == 3 or r == 6 or c == 3 or c == 6:
                    ans += 4
                else:
                    ans += 5
        

            


    print(ans)

