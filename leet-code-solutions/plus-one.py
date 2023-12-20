class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        last_digit = digits[-1]
        last_digit += 1
        if last_digit == 10:
            digits = int("".join(map(str, digits)))
            digits += 1
            digits = str(digits)
            digits = list(map(int, digits))
        else:
            digits[-1] = last_digit

        return digits