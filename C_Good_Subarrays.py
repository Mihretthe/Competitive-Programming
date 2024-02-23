for _ in range(int(input())):
    length = int(input())
    nums = list(map(int, list(input())))

    prefix = [0]

    for i in range(length):
        prefix.append(prefix[-1] + nums[i])

    # print(prefix)
    # print()
    
    count = 0

    for i in range(length + 1):
        left = 0
        right = i
        # if prefix[right] - right == 0:
        #     count += 1

        while left < right:
            if (prefix[right] - prefix[left]) == (right - left):
                count += 1

            left += 1

    print(count)
