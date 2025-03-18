class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:

        def calculate(left, right, alice):
            if alice:
                if left == right:
                    return nums[left]
                left_val = nums[left] + calculate(left + 1, right, not alice)
                right_val = nums[right] + calculate(left, right - 1, not alice)

                return max(left_val, right_val)                
            else:
                if left == right:
                    return nums[right]
                left_val = -nums[left] + calculate(left + 1, right, not alice)
                right_val = -nums[right] + calculate(left, right - 1, not alice)
                
                return min(left_val, right_val)
            
        return (calculate(0, len(nums) - 1, True)) >= 0

        