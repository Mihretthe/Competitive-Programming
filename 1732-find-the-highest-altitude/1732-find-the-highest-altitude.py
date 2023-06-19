class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        nums=[0]
        for i in gain:
            nums.append(nums[-1]+i)
        return max(nums)
    