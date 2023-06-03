class Solution:
    def calculateTax(self, brackets: List[List[int]], income: int) -> float:
        """
        brackets - array
        for each brackets there is an upper and its persent
        brackets are already sorted by upper bound
        the first upper times the persent plus the others like the two consecutive differences
        times there persent each
        there is another given integer income reperesenting the amount of money you earned 
        the income is to bound the upper the person can not earn more than its income
        
        """
        tax=0
        idx=0
        for i in range(len(brackets)):
            if brackets[i][0]>=income:
                idx=i
                break
        brackets[idx][0]=income  
        brackets=brackets[:idx+1]
        l=len(brackets)-1
        while l>0:
            tax+=(brackets[l][0]-brackets[l-1][0])*(brackets[l][1]/100)
            l-=1
        tax+=brackets[0][0]*brackets[0][1]/100
        return tax
            
       
        