class Solution:
    def romanToInt(self, s: str) -> int:
        romanNumbers = {"I" : 1, "V" : 5, "X" : 10, "L" : 50, "C" : 100, "D" : 500, "M" : 1000}
        r = len(s) - 1
        num = 0
        while r >= 0:
            if r > 0 and s[r] == "V" and s[r - 1] == "I":
                num += 4
                r -= 2
            elif r > 0 and s[r] == "X" and s[r - 1] == "I":
                num += 9
                r -= 2
            elif r > 0 and s[r] == "L" and s[r - 1] == "X":
                num += 40
                r -= 2
            elif r > 0 and s[r] == "C" and s[r - 1] == "X":
                num += 90
                r -= 2
            elif r > 0 and s[r] == "D" and s[r - 1] == "C":
                num += 400
                r -= 2
            elif r > 0 and s[r] == "M" and s[r - 1] == "C":
                num += 900
                r -= 2
            else:
                num += romanNumbers[s[r]]
                r -= 1
        return num
