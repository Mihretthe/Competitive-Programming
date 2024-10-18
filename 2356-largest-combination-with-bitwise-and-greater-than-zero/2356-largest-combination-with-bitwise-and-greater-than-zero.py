class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        bitwise = [0] * 32

        def calc(num):

            for i in range(32):
                bit_val = bool(num & 1 << i)
                bitwise[i] += bit_val
        
        for num in candidates:
            calc(num)
        
        return max(bitwise)