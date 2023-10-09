class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        counter = Counter(nums)
        if target not in counter:
            return [-1,-1]
        idx = nums.index(target)
        return [idx, idx + counter[target] - 1]