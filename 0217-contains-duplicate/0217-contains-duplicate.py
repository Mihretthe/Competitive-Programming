class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        a=Counter(nums)
        a=set(a.values())
        a=[i for i in a if i>1]
        return len(a)>0