nums = [4,3,7,8,6,0,2,1,5]

slow = 0
fast = 2
length = 9

while fast < length:
    print(slow, fast)
    if nums[slow] == nums[fast]:
        print( "Cycle")
        break
    slow = nums[slow]
    fast = nums[fast]
    fast = nums[fast]

    

