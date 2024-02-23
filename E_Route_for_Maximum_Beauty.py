from collections import defaultdict

for _ in range(int(input())):
    length = int(input())
    beauties = list(map(int, input().split()))

    sorted_beauties = sorted(beauties)[-3:]

    count = 0
    left = 0


    for i in range(length):
        if count == 3:
            print(sum(sorted_beauties) - (i- 1 - left))
            break
        
        if beauties[i] in sorted_beauties:
            if count == 0:
                left = i
            count += 1
    else:
        print(sum(sorted_beauties) - (length - left - 1))