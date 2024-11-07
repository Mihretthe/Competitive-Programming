class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        bit = [0] * 32

        for i in range(32):
            for candidate in candidates:
                bit[i] += int(bool(candidate & 1 << i))

        return max(bit)