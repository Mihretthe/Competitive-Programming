class Solution:
    def addDigits(self, num: int) -> int:
        s=str(num)
        a=0
        for i in s:
            a+=int(i)
        if len(str(a))==1:
            return a
        return self.addDigits(a)