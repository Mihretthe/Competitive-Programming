class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        def calculateScore(left, right, Turn):
            if Turn:
                if left == right:
                    return nums[left]                
                left_val = calculateScore(left + 1, right, False) + nums[left]
                right_val = calculateScore(left, right - 1, False) + nums[right]

                return max(left_val, right_val)
            else:
                if left == right:
                    return -nums[left]                
                left_val = calculateScore(left + 1, right, True) - nums[left]
                right_val = calculateScore(left, right - 1, True) - nums[right]

                return min(left_val, right_val)

        answer = calculateScore(0, len(nums) - 1, True)

        return answer >= 0
