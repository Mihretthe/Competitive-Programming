s = list(input())
length = len(s)
letters = "abcdefghijklmnopqrstuvwxyz"

left = 0
right = 1

while right < length:
    if s[left] == s[right]:
        end = right + 1
       
        for i in letters:
            if end < length:
                if i != s[end] and i!= s[right]:
                    s[right] = i
                    break
            else:
                if i != s[left]:
                    s[right] = i
                    break
    left += 1
    right += 1

print("".join(s))
        
                   
    