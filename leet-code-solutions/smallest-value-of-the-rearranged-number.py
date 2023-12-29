class Solution:
    def smallestNumber(self, num: int) -> int:
        if num >= 0:
            num = str(num)
            num = sorted(num)
            s = ""
            z = ""
            for i in num:
                if i == "0":
                    z += i
                else:
                    s += i
            s = s[:1] + z + s[1:]
            num = int(s)
        else:
            num = 0 - num
            num = int("".join(sorted(str(num), reverse = True)))
            num = 0 - int(num)            

        return num
