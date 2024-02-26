class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            n = 0 - n
            x = 1 / x

        if n < 1:
            return 1
        if n == 1:
            return x  % 1000000007

        if n % 2 == 0:
            return ((self.myPow(x, n // 2) % 1000000007) ** 2)  % 1000000007
        return ((self.myPow(x, n // 2) % 1000000007) ** 2 * x)  % 1000000007

    def countGoodNumbers(self, n: int) -> int:
        if n % 2 == 0:
            return (self.myPow(5, n // 2) * self.myPow(4, n // 2)) % 1000000007
        return (5 * self.myPow(5, n // 2) * self.myPow(4, n // 2)) % 1000000007

        