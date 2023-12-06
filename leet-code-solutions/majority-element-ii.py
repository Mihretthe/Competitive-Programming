class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        ans = []
        n = len(nums) // 3
        counter = Counter(nums)
        for i in counter:
            if counter[i] > n:
                ans.append(i)

        return ans