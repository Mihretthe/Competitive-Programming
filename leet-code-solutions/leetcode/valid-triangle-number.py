class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        length = len(nums)
        answer = 0

        for i in range(length - 1, 1, -1):
            left = 0
            right = i - 1
            while left < right:
                if nums[right] + nums[left] <= nums[i]:
                    left += 1
                else:
                    answer += right - left
                    right -= 1

        return answer