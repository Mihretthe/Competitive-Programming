class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        x=list(())
        # j=0
        for i in nums:
            count=0
            for j in nums: 
                if(i>j and j!=i):
                    count+=1
            x.append(count)
        return x
                
                
        