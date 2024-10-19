class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        init = "0"

        def reverse(s):
            return s[::-1]
        
        def invert(s):
            new = []
            for i in s:
                if i == "1":
                    new.append("0")
                else:
                    new.append("1")
            return "".join(new)

        for _ in range(n - 1):
            init = init + "1" + reverse(invert(init))
        
        return init[k - 1]