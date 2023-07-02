class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        """
        skill integer array even length
                
        """
        l=0
        r=len(skill)-1
        a=[]
        checker=set()
        skill.sort()
        while l<r:
            checker.add(skill[l]+skill[r])
            if len(checker)>1:
                return -1
            a.append([skill[l],skill[r]])
            l+=1
            r-=1
        a=[i[0]*i[1] for i in a]
        return sum(a)