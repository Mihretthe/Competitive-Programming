class Solution:
    def isHappy(self, n: int) -> bool:

        if n < 10 and n == 1:
            return True
        elif n < 10 and n % 2 == 0:
            return False
       
        
        s = str(n)
        n = 0
        for i in s:
            n += int(i) * int(i)

        return self.isHappy(n)
        
        



      

