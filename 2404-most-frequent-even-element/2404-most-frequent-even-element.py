class Solution:
    def maxm(self, a):
        b=[]
        a.sort()
        i=0
        while i<len(a):
            b.append(a.count(a[i]))
            i+=a.count(a[i])
        
        b.sort()
        return b[-1]
        
            
    def mostFrequentEven(self, nums: List[int]) -> int:
        nums.sort()
        a=[]
        for i in nums:
            if i%2==0:
                a.append(i)
        if a:
            x=self.maxm(a)
            for i in a:
                if a.count(i)==x:
                    return i
        else:
            return -1