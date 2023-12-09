for _ in range(int(input())):
    
    s = list(input())

    lower = set("acdefghijklmnopqrstuvwxyz")
    upper = set("ACDEFGHIJKLMNOPQRSTUVWXYZ")

    up = []
    low = []
 
 
    for i in range(len(s)):
        if s[i] == "b":
            s[i] = ""
            if low:
                s[low.pop()] = ''
        elif s[i] == "B":
            s[i] = ""
            if up:
                s[up.pop()] = ''
        if s[i] in lower:
            low += [i]
        elif s[i] in upper:
            up += [i]


 
    print("".join(s))
    


    






        
                


    