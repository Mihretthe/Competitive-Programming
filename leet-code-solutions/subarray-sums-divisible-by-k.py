class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        pre_mod = {0:1}
        prefix_sum = 0
        no_subarrays = 0

        for num in nums:
            prefix_sum += num
            mod = prefix_sum % k
            if mod in pre_mod:
                no_subarrays += pre_mod[mod]
                pre_mod[mod] += 1
            else:
                pre_mod[mod] = 1

        return no_subarrays
