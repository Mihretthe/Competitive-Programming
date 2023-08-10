class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        reminder ={0:1}
        count = 0
        current = 0
        for i in nums:
            current += i
            mod = current % k
            if mod < 0:
                mod += k
            if mod in reminder:
                count += reminder[mod]
                reminder[mod] += 1
            else:
                reminder[mod] = 1
        return count