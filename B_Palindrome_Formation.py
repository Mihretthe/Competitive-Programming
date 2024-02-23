for _ in range(int(input())):
    length = int(input())
    s = list(map(int, list(input())))

    left = 0
    right = length - 1
    flag = False
    flag2 = False
    count2 = 0

    while left < right:
        if flag:
            if flag2:
                if s[left] != s[right]:
                    print("No")
                    break
            else:                
                if s[left] == s[right]:
                    flag2 = True
            left += 1
            right -= 1
        else:
            if s[left] == s[right]:
                left += 1
                right -= 1
            elif s[left] != s[right]:
                flag = True
                left += 1
                right -= 1
    else:
        print("Yes")




