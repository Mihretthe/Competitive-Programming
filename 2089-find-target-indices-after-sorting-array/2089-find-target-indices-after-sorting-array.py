class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        x=list()
        for i in range(len(nums)):
            if nums[i]== target:
                x.append(i)
                x.sort()
        return x
            