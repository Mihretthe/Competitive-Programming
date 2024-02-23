for _ in range(int(input())):
    length = int(input())
    nums = list(map(int, input().split()))

    right = 0
    min_operation = 0
    sum = 0

    while right < length:
        if nums[right] >= 0:
            sum += nums[right]
            right += 1
        else:
            while right < length and nums[right] <= 0:
                sum += (0 - nums[right])
                right += 1
            
            min_operation += 1

    
    print(sum, min_operation)

