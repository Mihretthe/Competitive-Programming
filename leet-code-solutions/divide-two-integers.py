class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        quotient = dividend / divisor
        if quotient > 0:
            quotient = floor(quotient)
        else:
            quotient = ceil(quotient)

        if quotient > ((2**31) - 1):
            return ((2**31) - 1)
        elif quotient < (-2 ** 31):
            return (-2 ** 31)

        
        return quotient
