def counter(string, pattern):
    count = 0
    for i in range(len(string) - 6):
        a = string[i: i + 7]
        if a == pattern:
            count += 1
 
    return count

def map_string(string, pattern):
    string = list(string)
    for i in range(len(string)):
        if string[i] == "?":
            string[i] = pattern[i]
    string = "".join(string)

    return string


testcase = int(input())

for _ in range(testcase):
    n = int(input())
    s = input()
    pattern = "abacaba"

    count = counter(s, pattern) 

    if count == 1:
        s = s.replace("?", "d")
        print("Yes")
        print(s)

    elif count > 1:
        print("No")

    else:
        for i in range(n - 6):
            t = map_string(s[i:i + 7], pattern)            
            b = s[:i] + t + s[i+7:]
            if counter(b, pattern) == 1:
                b = b.replace("?", "d")
                print("Yes")
                print(b)
                break
        else:
            print("No")

                







































  

    # if n < 7:
    #     print("No")
    # else:
    #     if "abacaba" in s:
    #         count = 0
    #         for i in range(n - 6):
    #             if s[i:i + 7] == "abacaba":
    #                 count += 1
    #         if count == 1:
    #             print("Yes")
    #             if "?" in s:
    #                 s = s.replace("?","z")
    #             print(s)
    #         else:
    #             print("No")
        
    #     elif "???????" in s:
    #         print("Yes")
    #         s = s.replace("???????", "abacaba")
    #         if "?" in s:
    #             s = s.replace("?", "z")
    #         print(s)
    #     else:
    #         a = ""
    #         value = "abacaba"            
    #         c = 0
    #         for i in range(n):
    #             if s[i] == value[c] or s[i] == "?":
    #                 if s[i] == "?":
    #                     a += value[c]
    #                 else:
    #                     a += s[i]
    #                 c += 1
    #             else:
    #                 c = 0
    #                 a = ""
    #                 if s[i] == value[c]:
    #                     a += s[i]
    #                     c += 1                    
                
    #             if a == value:
    #                 print("Yes")
                    
    #                 print(s[:i - 6] + a + s[i + 1:])
    #                 break
    #             if c >= 7:
    #                 break
    #         else:
    #             if a == value:
    #                 print("Yes")
    #             else:
    #                 print("No")


