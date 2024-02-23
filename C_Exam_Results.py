from collections import Counter

length = int(input())
nums = list(map(int, input().split()))
counter = Counter(nums)

if len(counter) == length:
    print(length - 1)
else:
    nums.sort()
    h = length // 2

    first = nums[:h]
    second = nums[h:]
    
    f = 1
    s = 0
    if first:   
        new_array = [first[0]]
    
    while f < h and s < h:
        if first[f] == new_array[-1]:
            new_array.append(second[s])
            s += 1
        else:
            new_array.append(first[f])
            f += 1
    while s < len(second):
        new_array.append(second[s])
        s += 1

    happy = 0
    for i in range(1, length):
        if new_array[i] > new_array[i - 1]:
            happy += 1
 
    print(happy)

        

    