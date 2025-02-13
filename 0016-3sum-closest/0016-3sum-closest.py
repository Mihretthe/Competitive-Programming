class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        # First sort the array, so that we can loop through the array and find the for every element a two sum for that element 

        nums.sort()
        length = len(nums)
        diff = -inf
        ans = inf
        
        for i in range(length):
            left = i + 1
            right = length - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total == target:
                    return total
                if abs(target - total) < abs(target - ans):
                    ans = total
                    diff = abs(target - total)
                if total < target:
                    left += 1
                else:
                    right -= 1

        return ans