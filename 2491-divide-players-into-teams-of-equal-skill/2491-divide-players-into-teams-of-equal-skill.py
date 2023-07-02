class Solution:
    def dividePlayers(self, skill: List[int]) -> int:      
        l=0
        r=len(skill)-1
        a=0       
        skill.sort()
        checker=(skill[l]+skill[r])
        while l<r:
            if checker!=skill[l]+skill[r]:
                return -1
            a+=(skill[l]*skill[r])
            l+=1
            r-=1
        return a