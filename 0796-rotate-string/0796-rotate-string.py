class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if s==goal:
            return True
        i=0
        while i<len(s):
            if s[1:]+s[0]==goal:
                return True
            else:
                s=s[1:]+s[0]
            i+=1
        return False