class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        l = 0
        r = len(skill) - 1
        ans = 0
        chemistry = skill[0] + skill[-1]

        while l < r:
            if chemistry == skill[l] + skill[r]:
                ans += skill[l] * skill[r]
                l += 1
                r -= 1
            else:
                return -1
        return ans 