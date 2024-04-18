def findPreviousGreater(nums):
    #using monotonic strictly decreasing stack

    length = len(nums)
    previousGreater = [-1] * length
    stack = []

    for i in range(length):

        while stack and nums[stack[-1]] <= nums[i]:
            stack.pop()

        if stack:
            previousGreater[i] = nums[stack[-1]]

        stack.append(i)

    return previousGreater

print(findPreviousGreater([13, 8, 1, 5, 2, 5, 9, 7, 6, 12]))