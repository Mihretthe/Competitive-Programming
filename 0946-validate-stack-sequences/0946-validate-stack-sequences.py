class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        a=[]
        count=0
        for i in pushed:
            a.append(i)
            while a and a[-1]==popped[count]:
                a.pop()
                count+=1
        return count==len(popped)