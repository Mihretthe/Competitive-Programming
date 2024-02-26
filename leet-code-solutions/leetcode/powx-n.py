class Solution:
    def myPow(self, x: float, n: int) -> float:

        flag = False
        if n < 0:
            flag = True
            n = 0 - n

        if n < 1 and not flag:
            return 1
        if n == 1:
            if flag:
                return 1 / x
            return x

        val = self.myPow(x, n // 2) 

        if n % 2 == 0:
            if flag:
                return 1 / (val * val)
            else:
                return val * val
        if flag:
            return 1 / (val * val * x)
        return val * val * x