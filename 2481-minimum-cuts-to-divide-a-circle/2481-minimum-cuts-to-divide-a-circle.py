class Solution:
    def numberOfCuts(self, n: int) -> int:
        """
        a cut can be:
            to the teg
            to the center
        return the minimum number of cuts needed to divide a circle in to n equal parts
        4 we can use the two tig to tig or four halfs so we use min(tig,half)
        one circle lets assume the area is 1 unit the if we want to devid the
        circle n times one area should be 1/n
        odd:
            
        even:
            
        IF N==1:
            return 0
        elif n%2==0:
            return n/2
        elif n%2!=0:
            return n
        """
        if n==1:
            return 0
        elif n%2==0:
            return n//2
        else:
            return n