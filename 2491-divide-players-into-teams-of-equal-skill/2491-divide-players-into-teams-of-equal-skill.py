class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        
        
        equal = skill[0] + skill[len(skill) - 1]
        chemistry = skill[0] * skill[len(skill) - 1]
        
        l = 1
        r = len(skill) - 2
        while l < r:
            if skill[l] + skill[r] == equal:
                chemistry += (skill[l] * skill[r])
            else:
                return -1
            l += 1
            r -= 1
        return chemistry
        