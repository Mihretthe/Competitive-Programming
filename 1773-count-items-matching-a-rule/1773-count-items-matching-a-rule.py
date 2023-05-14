class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        i=0
        c=0
        if ruleKey=="type":
            i=0
        elif ruleKey=="color":
            i=1
        elif ruleKey=="name":
            i=2
        for j in items:
            if j[i]==ruleValue:
                c+=1
        return c
            
        
        
        
        # return len([x for x in items if ruleValue in x])
    