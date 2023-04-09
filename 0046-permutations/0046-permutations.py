class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        perm=list((permutations(nums)))
        return perm