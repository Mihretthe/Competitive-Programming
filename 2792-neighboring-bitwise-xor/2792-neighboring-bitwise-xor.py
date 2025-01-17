class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        

        xor = 0

        for i in derived:
            xor ^= i

        return xor == 0
