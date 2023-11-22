class Solution:
    def isHappy(self, n: int) -> bool:
        n = str(n)
        s = 0
        for i in n:
            s += int(i) * int(i)
        if len(str(s)) == 1 and s == 1:
            return True
        elif len(str(s)) == 1 and s % 2== 0:
            return False
        else:
            return self.isHappy(s)
        
        