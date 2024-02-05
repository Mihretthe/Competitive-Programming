class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        
        def cycle(nums):
            length = len(nums)

            for i in range(length):
                if nums[i] == i or nums[i] == -1001 or nums[i] == -1001:
                    continue
                slow = nums[i]
                fast = nums[i]               

                while fast < length:
                    if nums[slow] == -1001 or nums[fast] == -1001 or nums[nums[fast]] == -1001:
                        break
                    slow = nums[slow]
                    fast = nums[fast]
                    fast = nums[fast]
                
                    if slow == fast:
                        return True
            return False

        length = len(nums)

        positives = []
        for i in nums:
            if i == length:
                positives.append(-1001)
                continue
            if i > 0:
                positives.append(i)
            else:
                positives.append(-1001)


        negatives = []
        for i in nums:
            if i == -1 * length:
                negatives.append(-1001)
                continue
            if i < 0:
                negatives.append(i)
            else:
                negatives.append(-1001)

        def change(nums):
            length = len(nums)
            for i in range(length):
                if nums[i] == -1001:
                    continue
                nums[i] = (i + nums[i]) % length

            return nums
        positives = change(positives)
        negatives = change(negatives)

        print(positives, negatives)

        return cycle(positives) or cycle(negatives)


                